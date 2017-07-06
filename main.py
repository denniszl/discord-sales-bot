import discord
import os

from discord.ext.commands import Bot

my_bot = Bot(command_prefix="!")

@my_bot.event
async def on_read():
    print("Client logged in")

# TODO: potentially refactor this to enforce use of the numbered discriminator.
@my_bot.command(pass_context=True)
async def add_to_sale(ctx, *args):
    if len(args) != 2:
        return await my_bot.say('Usage: !add_to_sale \{discord_name\} \{sale\}')
    server = ctx.message.server
    if server.get_member_named(args[0]):
        if discord.utils.get(server.roles, name=args[1]):
            return_string = 'Adding user {} to sale {}'.format(args[0], args[1])
        else:
            return await my_bot.say('Sale {} doesn\'t exist.'.format(args[1]))
    else:
        return await my_bot.say('Can\'t find user named {}'.format(args[0]))
    return await my_bot.say(return_string)

if 'DISCORD_BOT_KEY' not in os.environ:
    print('Set the DISCORD_BOT_KEY environment variable to the key for your bot.')

my_bot.run(os.environ['DISCORD_BOT_KEY'])
