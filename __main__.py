from loguru import logger
from source.Base.Bot.bot import start

__version__ = "1.0.0+2022.02" # <MAJOR>.<MINOR>.<PATCH>-<IDENTIFIER>.<IDENTIFIER>+<BUILDMETA>

start(__version__)