import random

import tanjun

component = tanjun.Component()


@component.with_slash_command
@tanjun.as_slash_command('flip', 'Flip a coin')
async def flip(ctx: tanjun.abc.SlashContext) -> None:
    await ctx.respond(f'{random.choice(("Heads", "Tails"))} 🪙')


loader = component.make_loader()
