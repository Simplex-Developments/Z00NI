from loguru import logger
from ..Helper.extloader import extloader

def __init__(bot, version):
    exts = []
    extloader(bot, exts)