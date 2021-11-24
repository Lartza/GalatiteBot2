# GalatiteBot2
Custom Discord bot for the Galatite Order - an Elder Scrolls Online guild.

## Commands
Command | Description | Arguments
--- | --- | ---
/agree | Agree to the rules | None
/flip | Flip a coin | None
/order | Randomize the order of options | `options, Space separated list of options`
/pick | Pick a random option | `options, Space separated list of options`
/ping | Pong! (A silly little game) | None
/random | Get a random number. Default 1-100 | `minimum, optional` `maximum, optional`
/roll | Roll a die | None

## Running the bot
Create a venv, install requirements from requirements.txt, copy config.py.example to config.py and edit as needed.

If you have access to a compiler optionally install hikari[speedups]

On UNIX optionally install uvloop