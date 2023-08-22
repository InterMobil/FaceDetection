import logging

def get_logger(log_name, level=logging.DEBUG):

    formatter = logging.Formatter('[%(asctime)s] %(levelname)-8s %(name)s.%(funcName)s:%(lineno)-d :: %(message)s')
    file_name = 'logs/app.log'

    handler = logging.FileHandler(file_name)
    handler.setFormatter(formatter)

    specified_logger = logging.getLogger(log_name)
    specified_logger.setLevel(level)
    specified_logger.addHandler(handler)

    return specified_logger