import random

import tanjun

component = tanjun.Component()


@component.with_slash_command
@tanjun.as_slash_command('roll', 'Roll a die')
async def roll(ctx: tanjun.abc.SlashContext) -> None:
    await ctx.respond(f'{random.randint(1, 6)} 🎲')


loader = component.make_loader()
