import logging
import os
import re
from pathlib import Path

import hikari
from hikari import Intents
from hikari.snowflakes import Snowflake
import tanjun
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import config
from jobs import crow, reddit

if os.name != 'nt':
    import uvloop
    uvloop.install()

logger = logging.getLogger('galatitebot')
scheduler = AsyncIOScheduler()

my_intents = (
    Intents.ALL_UNPRIVILEGED |
    Intents.GUILD_MEMBERS
)

bot = hikari.GatewayBot(config.TOKEN, intents=my_intents)
client = tanjun.Client.from_gateway_bot(bot, declare_global_commands=Snowflake(config.GUILD_ID))
client.load_modules(*Path('modules').glob('*.py'))


@bot.listen()
async def on_shard_ready(_: hikari.ShardReadyEvent) -> None:
    # scheduler.add_job(crow.run, 'cron', minute='*/1', args=[bot.rest], id='crow')
    # scheduler.add_job(reddit.run, 'cron', minute='*/1', args=[bot.rest], id='reddit')
    scheduler.start()


@bot.listen()
async def on_stopping(_: hikari.StoppingEvent) -> None:
    scheduler.shutdown()


@bot.listen()
async def react(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return

    if re.search(r'\b(hello|hi|hey|greetings|good( morning| night| evening| day|bye))\b', event.content, re.I | re.M) \
            and not re.search(r"(\bnot|n'?t)\b", event.content, re.I | re.M):
        await event.message.add_reaction('👋')

    if re.search(r'\bb(irth)?day', event.content, re.I | re.M):
        await event.message.add_reaction('🎂')


if __name__ == '__main__':
    bot.run()
