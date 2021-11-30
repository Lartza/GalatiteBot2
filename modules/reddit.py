import hikari
import tanjun

from galatitebot.checks import role_check
import jobs.reddit

component = tanjun.Component()


@component.with_slash_command
@tanjun.with_check(role_check)
@tanjun.as_slash_command('reddit', 'Admin only test command')
async def help_command(ctx: tanjun.abc.SlashContext) -> None:
    await jobs.reddit.run(ctx.rest)
    await ctx.create_initial_response('Posted or errored!', flags=hikari.MessageFlag.EPHEMERAL)


loader = component.make_loader()
