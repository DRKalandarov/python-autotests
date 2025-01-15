import datetime

import logging
import logging.handlers

from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get("timestamp"):
            log_record["timestamp"] = datetime.datetime.now()
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname


def file_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = CustomJsonFormatter(
        fmt="%(timestamp)s %(level)s %(module)s %(message)s %(threadName)s",
        json_ensure_ascii=False,
    )

    debug_handler = logging.handlers.RotatingFileHandler(
        filename="./tests/resources/logs/debug.log",
        mode="a",
        maxBytes=10485760,  # 10MB
        backupCount=5,
        encoding="utf-8",
    )
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)

    info_handler = logging.handlers.RotatingFileHandler(
        filename="./tests/resources/logs/info.log",
        mode="a",
        maxBytes=10485760,  # 10MB
        backupCount=5,
        encoding="utf-8",
    )
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)

    logger.addHandler(debug_handler)
    logger.addHandler(info_handler)

    return logger
