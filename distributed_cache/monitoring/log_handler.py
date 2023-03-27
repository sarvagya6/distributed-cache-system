# import logging

# def setup_logging():
#     logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

# def log(level, message):
#     if level.lower() == "debug":
#         logging.debug(message)
#     elif level.lower() == "info":
#         logging.info(message)
#     elif level.lower() == "warning":
#         logging.warning(message)
#     elif level.lower() == "error":
#         logging.error(message)
#     elif level.lower() == "critical":
#         logging.critical(message)

import logging

class LogHandler:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        
        self.logger.addHandler(ch)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
