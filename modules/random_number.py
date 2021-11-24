import random

import tanjun

component = tanjun.Component()


@component.with_slash_command
@tanjun.with_int_slash_option('minimum', 'Minimum number', default=1)
@tanjun.with_int_slash_option('maximum', 'Maximum number', default=100)
@tanjun.as_slash_command('random', 'Get a random number. Default 1-100')
async def random_number(ctx: tanjun.abc.SlashContext, minimum: int, maximum: int) -> None:
    await ctx.respond(random.randint(minimum, maximum))


loader = component.make_loader()
