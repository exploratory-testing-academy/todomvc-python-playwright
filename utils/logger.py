import logging

logging.getLogger("faker").setLevel(logging.ERROR)
logging.getLogger('asyncio').setLevel(logging.WARNING)


class Logger:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def debug(self, msg, *args, **kwargs):
        self.log.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.log.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.log.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.log.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.log.critical(msg, *args, **kwargs)
