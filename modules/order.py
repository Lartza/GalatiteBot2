import random

import tanjun

component = tanjun.Component()


@component.with_slash_command
@tanjun.with_str_slash_option('options', 'Space separated list of options')
@tanjun.as_slash_command('order', 'Randomize the order of options')
async def order(ctx: tanjun.abc.SlashContext, options: str) -> None:
    options = options.split()
    random.shuffle(options)
    await ctx.respond(' '.join(options))


loader = component.make_loader()
