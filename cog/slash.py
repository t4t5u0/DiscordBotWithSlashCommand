import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="neko", description="にゃーんと鳴くやつ")
    async def neko(self, ctx: SlashContext):
        "にゃーんと鳴くやつ"
        # embed = discord.Embed(title="鳴き声")
        await ctx.send(content=f"{ctx.author.mention} にゃーん")

    @cog_ext.cog_slash(name="echo",
                       description="引数を1つ受け取り、そのまま返す",
                       options=[
                           create_option(
                               name="arg",
                               description="引数",
                               option_type=3,
                               required=True
                           )
                       ])
    async def echo(self, ctx: SlashContext, arg: str):
        "引数を1つ受け取り、そのまま返す"
        await ctx.send(content=arg)

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("pong")


def setup(bot):
    bot.add_cog(Slash(bot))
