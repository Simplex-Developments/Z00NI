from loguru import logger
from source.Bot.bot import start

__version__ = "0.2.0-b.1+2022.02" # <MAJOR>.<MINOR>.<PATCH>-<IDENTIFIER>.<IDENTIFIER>+<BUILDMETA>

start(__version__)