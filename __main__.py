from loguru import logger
from source.Base.Bot.bot import start

__version__ = "1.0.0+2022.02" # <MAJOR>.<MINOR>.<PATCH>-<IDENTIFIER>.<IDENTIFIER>+<BUILDMETA>
exts        = [
            
            ]


start(__version__)