from nextcord.ext import commands
from nextcord.ext.commands import  Context
from nextcord import Embed, Colour

from ..Base.Helper.dev import load, unload, reload
from ..Base.Helper.checks import is_dev

class developer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="load", aliases=["enable", "l"])
    @is_dev()
    async def load(self, ctx: Context, *args):
        """Loads a Cog"""
        await ctx.message.delete()
        embed = Embed(title="Load | Lade...", colour=Colour.orange(), timestamp=ctx.message.created_at)
        msg = await ctx.send(embed=embed)
        embed = Embed(title="Load | Ergebnisse", colour=Colour.green(), timestamp=ctx.message.created_at)
        for _num, _arg in enumerate(args):
            result = load(self, _arg)
            embed.add_field(name=f"`{_arg.upper()}` Load | Ergebnis", value=result, inline=False)
        await msg.edit(embed=embed, delete_after=8)

    @commands.command(name="unload", aliases=["disable", "unl"])
    @is_dev()
    async def unload(self, ctx: Context, *args):
        """Unloads a Cog"""
        await ctx.message.delete()
        embed = Embed(title="Unload | Lade...", colour=Colour.orange(), timestamp=ctx.message.created_at)
        msg = await ctx.send(embed=embed)
        embed = Embed(title="Unload | Ergebnisse", colour=Colour.green(), timestamp=ctx.message.created_at)
        for _num, _arg in enumerate(args):
            result = unload(self, _arg)
            embed.add_field(name=f"`{_arg.upper()}` Unload | Ergebnis", value=result, inline=False)
        await msg.edit(embed=embed, delete_after=8)

    @commands.command(name="reload")
    @is_dev()
    async def reload(self, ctx: Context, *args):
        """Reloads a Cog"""
        await ctx.message.delete()
        embed = Embed(title="Reload | Lade...", colour=Colour.orange(), timestamp=ctx.message.created_at)
        msg = await ctx.send(embed=embed)
        embed = Embed(title="Reload | Ergebnisse", colour=Colour.green(), timestamp=ctx.message.created_at)
        for _num, _arg in enumerate(args):
            result = reload(self, _arg)
            embed.add_field(name=f"`{_arg.upper()}` Reload | Ergebnis", value=result, inline=False)
        await msg.edit(embed=embed, delete_after=8)

    async def cog_command_error(self, ctx, e):

        usage = "`load/unload/reload <Modul>`"
        perms = "`STAFF`"


        embed = Embed(title="Developer | Failure", colour=Colour.brand_red(), timestamp=ctx.message.created_at)

        if isinstance(e, commands.CommandError):
            embed.add_field(name=":warning: Fehler", value=f"Errorcode:\n> {e}", inline=False)
            embed.set_footer(text="Selbstzerst??rung der Nachricht in 8 Sekunden")

        if isinstance(e, commands.MissingRequiredArgument):
            embed.add_field(name=":page_facing_up: Fehlerhafte Nutzung:", value=f"\n> {usage}", inline=False)
            return await ctx.send(embed=embed, delete_after=8)

        if isinstance(e, commands.CheckFailure):
            embed.add_field(name=":lock: Fehlende Rechte:", value=f"Ben??tigte Rechte:\n> {perms}", inline=False)
            return await ctx.send(embed=embed, delete_after=8)    

def setup(bot):
    bot.add_cog(developer(bot))
    