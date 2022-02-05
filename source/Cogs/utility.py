from discord import AllowedMentions
from nextcord.ext import commands
import nextcord
from ..Base.Helper.checks import is_dev

class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.message.delete()

    @commands.command(name="say", allowed_mentions=AllowedMentions(everyone=False, users=False, roles=False, replied_user=False))
    async def say(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(text) # FIXME: AllowedMentions Fixen

    @commands.command(name="spam")
    @is_dev()
    async def spam(self, ctx, num, *, text):
        return

def setup(bot):
    bot.add_cog(utility(bot))