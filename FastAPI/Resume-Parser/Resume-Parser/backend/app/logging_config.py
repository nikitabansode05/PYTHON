import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logging():
    os.makedirs("logs",exist_ok=True)
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    # Console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    # File
    file_handler = RotatingFileHandler("logs/application.log",maxBytes=5 * 1024 * 1024,backupCount=5,encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    # Format
    formatter = logging.Formatter("%(asctime)s | ""%(levelname)-8s | ""%(name)-12s | ""%(message)s")
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    # Register
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)