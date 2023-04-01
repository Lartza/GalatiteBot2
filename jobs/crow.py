import hikari
import tanjun
import aiohttp
import alluka
from datetime import date

import config

component = tanjun.Component()


@component.with_schedule
@tanjun.as_time_schedule(hours=12, minutes=30)
async def run(client: alluka.Injected[tanjun.Client]) -> None:
    today = date.today()
    if today.day == 1 and today.month == 4:
        embed = (
            hikari.Embed(
                colour=hikari.Colour(0x0099ff),
                title='BRRRRRR RA-TA-TA-TA-TA-TA',
                description='[Tahoe Quarterly](https://tahoequarterly.com/features/as-the-old-crow-flies)'
            )
            .set_image('https://lartza.ltn.fi/Hero2.jpg')
            .set_footer(text='-American Crow')
        )
        await client.rest.create_message(config.CROW_CHANNEL, embed)
    elif config.UNSPLASH_ACCESS_KEY and (config.UNSPLASH_ACCESS_KEY is not None):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.unsplash.com/photos/random',
                                   headers={'Authorization': f'Client-ID {config.UNSPLASH_ACCESS_KEY}',
                                            'Accept-Version': 'v1'},
                                   params={'query': 'crow'}) as response:
                json = await response.json()
                embed = (
                    hikari.Embed(
                        colour=hikari.Colour(0x0099ff),
                        title='Ah-Ah-Aaaah',
                        description=f'Photo by [{json["user"]["name"]}](https://unsplash.com/@'
                                    f'{json["user"]["username"]}?utm_source=GalatiteBot&utm_medium=referral) on '
                                    '[Unsplash](https://unsplash.com/?utm_source=GalatiteBot&utm_medium=referral)'
                    )
                    .set_image(json['urls']['small'])
                    .set_footer(text='-Australian Crow')
                )
                await client.rest.create_message(config.CROW_CHANNEL, embed)
    else:
        embed = (
            hikari.Embed(
                colour=hikari.Colour(0x0099ff),
                title='Ah-Ah-Aaaah',
            )
            .set_footer(text='-Australian Crow',)
            .set_image('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Corvus_coronoides_-_Doughboy_Head.jpg'
                       '/220px-Corvus_coronoides_-_Doughboy_Head.jpg')
        )

        await client.rest.create_message(config.CROW_CHANNEL, embed)


loader = component.make_loader()
