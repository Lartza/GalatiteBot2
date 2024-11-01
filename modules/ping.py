import random
from typing import Tuple

import hikari
import tanjun

component = tanjun.Component()


async def ping_response(mention: str, rest: hikari.api.rest.RESTClient) ->\
        Tuple[str, hikari.api.special_endpoints.MessageActionRowBuilder]:
    msg = None
    rnd = random.randint(0, 99)

    if rnd < 85:
        hit_rnd = random.randint(0, 24)
        if hit_rnd == 0:
            msg = f"-PONG! {mention} hit the ball so hard :muscle:, {mention}'s racket broke. " \
                  f"But {mention} has a spare racket. \nThe game continues. :ping_pong:"
        elif hit_rnd == 1:
            msg = f'-Plash!... {mention} just used a fish :fish: to hit the ball... Guess that counts. \n' \
                  'The game continues! :ping_pong:'
        elif hit_rnd == 2:
            msg = f"-Stop. **Rigurt the Brash** needs {mention}'s help. He ordered fitting Ping-Pong " \
                  f"attire. Somehow it never arrived and he needs {mention} to investigate :mag:.\n" \
                  f"{mention} starts on a quest to find out what happened. \n{mention} finds a " \
                  "referee hiding something under the bench. It is a hat with a racket glued to it :tophat: " \
                  f":ping_pong:.\n{mention} gives the hat to **Rigurt the Brash** and the game continues!"
        elif hit_rnd == 3:
            msg = f'''-pong. {mention} hit the ball! :ping_pong:. \n
            The ball suddenly turns red :red_circle:. \n
            The ball says: "You probably don't recognize me, because of the red arm." \n
            Everyone keeps playing as if nothing has happened. \nThe game continues. :ping_pong:'''
        elif hit_rnd == 4:
            msg = f'-PONG!!!! {mention} gets angry and triggers his Super Saiyajin Mode ' \
                  f':man_supervillain:. \n{mention} almost breaks the table... but the game continues! ' \
                  ':ping_pong:'
        else:
            msg = f'-pong. {mention} hit the ball! :ping_pong:'
    elif rnd < 90:
        win_rnd = random.randint(0, 2)
        if win_rnd == 0:
            msg = '-pong! Dremora invade the earth and everyone was vaporized by Molag Bal :smiling_imp:. \nSince ' \
                  f'{mention} was the last to hit the ball, {mention} wins by ' \
                  f'vaporization-elimination! \nCongratulation to {mention}!!! :partying_face:'
        elif win_rnd == 1:
            msg = f'-Ohh no! {mention} missed. **Puff** It turns out, that {mention} was ' \
                  'Sheogorath in disguise the WHOLE TIME! :clown: \nSince Sheo is threatening me with a spoon right ' \
                  f'now: \n{mention} wins!!! :partying_face:'
        elif win_rnd == 2:
            msg = '01000100011011110010000001111001011011110111010100100000011010110110111001101111011101110010000001' \
                  '10100001101111011101110010000001101100011011110110111001100111001000000100100100100111011101100110' \
                  '01010010000001100010011001010110010101101110001000000110110001101111011011110110101101101001011011' \
                  '1001100111001000000110011001101111011100100010000001111001011011110111010100111111\n' \
                  '...ohh sorry... Did not see you there... I mean: \n' \
                  f'-Pong! {mention} wins! :partying_face:'
    elif rnd < 100:
        lose_rnd = random.randint(0, 9)
        if lose_rnd == 0:
            msg = f'-Ohh no... {mention} missed. \nLooks like {mention} has taken too much moon' \
                  f' sugar :woozy_face:. \n{mention} is out! :thumbsdown:'
        else:
            msg = f'-Ohh no... {mention} missed. \n{mention} is out! :thumbsdown:'

    row = rest.build_message_action_row()
    row.add_interactive_button(hikari.ButtonStyle.PRIMARY, '🏓', emoji='🏓')
    return msg, row


@component.with_slash_command
@tanjun.as_slash_command('ping', 'Pong! (A silly little game)')
async def ping(ctx: tanjun.abc.Context) -> None:
    msg, row = await ping_response(ctx.author.mention, ctx.rest)

    await ctx.respond(msg, component=row)


loader = component.make_loader()
