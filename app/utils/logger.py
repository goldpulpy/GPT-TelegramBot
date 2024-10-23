"""Logging module."""
import sys
import logging
from logging.handlers import RotatingFileHandler


def setup_logger(
    name: str,
    log_file: str = 'logs.txt',
    level: int = logging.INFO
) -> logging.Logger:
    """
    Configure and return a logger.

    :param name: name of the logger
    :param log_file: log file path
    :param level: logging level
    :return: logger object
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    file_handler = RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=5)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.propagate = False
    return logger
