import os

from robot.api import logger


class NothingLibrary:

    def log_path_to_console(self):
        path = os.environ.get("PATH")
        logger.info(path, also_console=True)
