from loguru import logger
from source.Base.Bot.bot import start

__version__ = "1.2.0-b+2022.02" # <MAJOR>.<MINOR>.<PATCH>-<IDENTIFIER>.<IDENTIFIER>+<BUILDMETA>
exts        = [
            "developer"
            ]


start(__version__, exts)