import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='logger.log',
    filemode='w'
)

logging.debug("debug info")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")
