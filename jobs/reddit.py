import hikari
import tanjun
import aiohttp

import config

component = tanjun.Component()


@component.with_schedule
@tanjun.as_time_schedule(hours=16, minutes=00)
async def run(client: tanjun.Client = tanjun.inject(type=tanjun.Client)) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.reddit.com/r/elderscrollsonline/top/.json?t=day') as feed_response:
            feed_json = await feed_response.json()
            link = feed_json['data']['children'][0]['data']['permalink']

            async with session.get('https://www.reddit.com' + link + '.json') as response:
                json = await response.json()
                data = json[0]['data']['children'][0]['data']

                if data['is_video']:
                    embed = (
                        hikari.Embed(
                            colour=hikari.Colour(0x0099ff),
                            title=data['title'],
                            url='https://www.reddit.com' + data['permalink'],
                            description='Videos not supported :(',
                        )
                    )
                else:
                    embed = (
                        hikari.Embed(
                            colour=hikari.Colour(0x0099ff),
                            title=data['title'],
                            url='https://www.reddit.com' + data['permalink'],
                            description=data['selftext'],
                        )
                    )

                    try:
                        embed.set_image(data['url_overridden_by_dest'])
                    except KeyError:
                        pass

                embed.set_author(name='u/' + data['author'])
                embed.set_footer(
                    text="This is today's top post of /r/elderscrollsonline.",
                )

                await client.rest.create_message(config.REDDIT_CHANNEL, embed)


loader = component.make_loader()
