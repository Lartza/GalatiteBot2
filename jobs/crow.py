import hikari
import aiohttp

import config


async def run(rest: hikari.api.rest.RESTClient) -> None:
    if config.UNSPLASH_ACCESS_KEY and (config.UNSPLASH_ACCESS_KEY is not None):
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
                await rest.create_message(config.CROW_CHANNEL, embed)
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

        await rest.create_message(config.CROW_CHANNEL, embed)
