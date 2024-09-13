import logging
import logging.handlers
import time

from flask import session

from CTFd.utils.user import get_ip


# Valid Severities: debug, info, warning, error, critical
def log(logger, severity, format, **kwargs):
    logger = logging.getLogger(logger)
    props = {
        "id": session.get("id"),
        "date": time.strftime("%m/%d/%Y %X"),
        "ip": get_ip(),
    }
    props.update(kwargs)
    msg = format.format(**props)
    if severity == "debug":
        logger.debug(msg)
    elif severity == "info":
        logger.info(msg)
    elif severity == "warning":
        logger.warning(msg)
    elif severity == "error":
        logger.error(msg)
    elif severity == "critical":
        logger.critical(msg)
    else:
        logger.warning(
            "Subsequent log message submitted with invalid severity. Defaulting to info"
        )
        logger.info(msg)
