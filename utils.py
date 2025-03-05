import logging

def get_logger():
    logger = logging.getLogger("gpm_logger")
    # Set logging level
    logger.setLevel(logging.DEBUG)
    # Set logging format 
    format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Setting terminal logging 
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO) 
    console_handler.setFormatter(format)

    # Setting file logging
    file_handler = logging.FileHandler("running.log", mode="a", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)  # 记录所有级别日志
    file_handler.setFormatter(format)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger
