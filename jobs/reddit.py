import os
import base64
import hikari
import tanjun
import aiohttp
import alluka

import config

component = tanjun.Component()

app_id = os.getenv("REDDIT_APP_ID")
app_secret = os.getenv("REDDIT_APP_SECRET")
app_username = os.getenv("REDDIT_APP_USERNAME")

TOKEN_URL = "https://www.reddit.com/api/v1/access_token"


@component.with_schedule
@tanjun.as_time_schedule(hours=16, minutes=00)
async def run(client: alluka.Injected[tanjun.Client]) -> None:
    if not app_id or not app_secret or not app_username:
        return

    auth = base64.b64encode(f"{app_id}:{app_secret}".encode()).decode()

    async with aiohttp.ClientSession() as session:
        async with session.post(
            TOKEN_URL,
            data={"grant_type": "client_credentials"},
            headers={
                "Authorization": f"Basic {auth}",
                "User-Agent": f"GalatiteBot2 (by /u/{app_username})",
            },
        ) as token_response:
            if token_response.status != 200:
                print(f"Failed to obtain token: {token_response.status}")
                return
            token_data = await token_response.json()
            access_token = token_data.get("access_token")

        if access_token:
            async with session.get(
                "https://oauth.reddit.com/r/elderscrollsonline/top/.json?t=day",
                headers={
                    "Authorization": f"bearer {access_token}",
                    "User-Agent": f"GalatiteBot2 (by /u/{app_username})",
                },
            ) as feed_response:
                if feed_response.status != 200:
                    print(f"Failed to fetch feed: {feed_response.status}")
                    return
                feed_json = await feed_response.json()
                link = feed_json["data"]["children"][0]["data"]["permalink"]

                async with session.get(
                    "https://oauth.reddit.com" + link + ".json",
                    headers={
                        "Authorization": f"bearer {access_token}",
                        "User-Agent": f"GalatiteBot2 (by /u/{app_username})",
                    },
                ) as response:
                    if response.status != 200:
                        print(f"Failed to fetch post details: {response.status}")
                        return
                    json = await response.json()
                    data = json[0]["data"]["children"][0]["data"]

                    if data["is_video"]:
                        embed = hikari.Embed(
                            colour=hikari.Colour(0x0099FF),
                            title=data["title"],
                            url="https://www.reddit.com" + data["permalink"],
                            description="Videos not supported :(",
                        )
                    else:
                        embed = hikari.Embed(
                            colour=hikari.Colour(0x0099FF),
                            title=data["title"],
                            url="https://www.reddit.com" + data["permalink"],
                            description=data.get("selftext", ""),
                        )

                        try:
                            embed.set_image(data["url_overridden_by_dest"])
                        except KeyError:
                            pass

                    embed.set_author(name="u/" + data["author"])
                    embed.set_footer(
                        text="This is today's top post of /r/elderscrollsonline.",
                    )

                    await client.rest.create_message(config.REDDIT_CHANNEL, embed)


loader = component.make_loader()
