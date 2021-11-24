import tanjun

component = tanjun.Component()


@component.with_slash_command
@tanjun.as_slash_command('help', 'Link to the documentation')
async def help(ctx: tanjun.abc.SlashContext) -> None:
    await ctx.respond('https://github.com/Lartza/GalatiteBot2#commands')


loader = component.make_loader()
