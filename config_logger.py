import logging

def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    file_handler = logging.FileHandler("app.log")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
