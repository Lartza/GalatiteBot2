import hikari
import tanjun

from galatitebot.checks import role_check
import jobs.reddit

component = tanjun.Component()


@component.with_slash_command
@tanjun.with_check(role_check)
@tanjun.as_slash_command('reddit', 'Admin only, force top reddit post job')
async def reddit(ctx: tanjun.abc.SlashContext) -> None:
    await ctx.create_initial_response('Posting!', flags=hikari.MessageFlag.EPHEMERAL)
    await jobs.reddit.run(ctx.rest)


loader = component.make_loader()
