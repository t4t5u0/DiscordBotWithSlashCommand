import configparser

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord_slash import SlashCommand


config = configparser.ConfigParser()
config.read('./config.ini')
TOKEN = config['TOKEN']['token']


bot: discord.ext.commands.Bot = Bot(command_prefix='/')
slash_client = SlashCommand(bot)
bot.load_extension("cog.slash")


@bot.event
async def on_ready():
    # Bot起動時にターミナルに通知を出す
    print('-'*20)
    print('ログインしました')
    print('-'*20)
    await bot.change_presence(activity=discord.Game(name='/help'))

if __name__ == '__main__':
    bot.run(TOKEN)
