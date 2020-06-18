import discord
from discord.ext import commands
from discord.ext.commands import Bot
import sys, traceback
import random


bot = commands.Bot(command_prefix='!')
initial_extensions = [
    'cogs.music',
    'cogs.chat',
]

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_ready():
    print(f'\n\nlogou como: {bot.user.name} - {bot.user.id}\n')
    await bot.change_presence(activity=discord.Game(name='!help'))
    print(f'{bot.user.name} ta on')


TOKEN = ""
bot.run(TOKEN , bot=True, reconnect=True)
