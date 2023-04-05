import hikari
import tanjun

import config

component = tanjun.Component()


@component.with_slash_command
@tanjun.as_slash_command('agree', 'Agree to the rules')
async def agree(ctx: tanjun.abc.SlashContext) -> None:
    role = 640289940462108672
    channel = config.WELCOME_CHANNEL

    if role in ctx.member.role_ids:
        await ctx.create_initial_response('You have already agreed to the rules and have been assigned the'
                                          ' Discord-Bound role.', flags=hikari.MessageFlag.EPHEMERAL)
    else:
        await ctx.member.add_role(role)
        await ctx.create_initial_response("Thank you for agreeing to our rules.", flags=hikari.MessageFlag.EPHEMERAL)
        await ctx.rest.create_message(channel, f"Greetings! Welcome to the Bantam Symposium! {ctx.author.mention},"
                                               " take a look around. There is always someone to help!"
                                               " We hope you'll have a majestic time here.")


loader = component.make_loader()
