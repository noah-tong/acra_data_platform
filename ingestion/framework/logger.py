import logging

from pathlib import Path

from config.config import LOG_PATH

LOG_PATH.mkdir(exist_ok=True)

LOG_FILE = LOG_PATH / "ingestion.log"


def get_logger(name):

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(

        "%(asctime)s | %(levelname)s | %(message)s"

    )

    file_handler = logging.FileHandler(LOG_FILE)

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()

    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger