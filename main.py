import logging
import os
import re
from pathlib import Path

import hikari
from hikari import Intents
from hikari.snowflakes import Snowflake
from hikari.interactions.base_interactions import ResponseType
import tanjun

import config
from modules.ping import ping_response

if os.name != 'nt':
    import uvloop
    uvloop.install()

logger = logging.getLogger('galatitebot')

my_intents = (
    Intents.ALL_UNPRIVILEGED |
    Intents.GUILD_MEMBERS |
    Intents.MESSAGE_CONTENT
)

bot = hikari.GatewayBot(config.TOKEN, intents=my_intents)
client = tanjun.Client.from_gateway_bot(bot, declare_global_commands=Snowflake(config.GUILD_ID))
client.load_modules(*Path('modules').glob('*.py'))
client.load_modules(*Path('jobs').glob('*.py'))


@bot.listen()
async def react(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return

    if re.search(r'\b(hello|hi|hey|greetings|good( morning| night| evening| day|bye))\b', event.content, re.I | re.M) \
            and not re.search(r"(\bnot|n'?t)\b", event.content, re.I | re.M):
        await event.message.add_reaction('👋')

    if re.search(r'\bb(irth)?day', event.content, re.I | re.M):
        await event.message.add_reaction('🎂')


@bot.listen()
async def ping_event(event: hikari.InteractionCreateEvent) -> None:
    if event.interaction.type == hikari.InteractionType.MESSAGE_COMPONENT and event.interaction.custom_id == '🏓':
        msg, row = await ping_response(event.interaction.user.mention, bot.rest)
        await event.interaction.create_initial_response(ResponseType.MESSAGE_UPDATE, components=[])
        await event.app.rest.create_message(event.interaction.channel_id, msg, component=row)


if __name__ == '__main__':
    bot.run()
