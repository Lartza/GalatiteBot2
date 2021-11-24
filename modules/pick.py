import random

import tanjun

component = tanjun.Component()


@component.with_slash_command
@tanjun.with_str_slash_option('options', 'Space separated list of options')
@tanjun.as_slash_command('pick', 'Pick a random option')
async def pick(ctx: tanjun.abc.SlashContext, options: str) -> None:
    await ctx.respond(random.choice(options.split()))


loader = component.make_loader()
