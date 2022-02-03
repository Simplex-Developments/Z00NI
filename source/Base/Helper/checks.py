from nextcord.ext.commands import Context, check

class ids():
    STAFFs = [
        int(579111799794958377)
        ]
    DEVs = [
        int(579111799794958377)
        ]
    BOTs = [
        int(924832290616508476),
        int(937481737750057011)
        ]

def is_dev():
    async def predicate(ctx: Context) -> bool:
        if not ctx.guild: return False

        return ctx.author.id in ids.DEVs

    return check(predicate)

def is_staff():
    async def predicate(ctx: Context) -> bool:
        if not ctx.guild: return False

        return ctx.author.id in ids.STAFFs

    return check(predicate)

def is_bot():
    async def predicate(ctx: Context) -> bool:
        if not ctx.guild: return False

        return ctx.author.id in ids.BOTs

    return check(predicate)
