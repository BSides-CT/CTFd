import logging
import logging.handlers
import time

from flask import session

from CTFd.utils.user import get_ip


# Valid Severities: debug, info, warning, error, critical
def log(logger, severity, format, **kwargs):
    # Standard properties used in the standard log prefix and available for custom message segments.
    props = {
        "id": session.get("id"),
        "date": time.strftime("%m/%d/%Y %X"),
        "ip": get_ip(),
        "severity": severity.upper(),
        "logger": logger.upper(),
    }
    # This is below props beause we are using logger as a string in props before it becomes a logger object.
    logger = logging.getLogger(logger)

    props.update(kwargs)
    # Putting the standard segment after props update allows override of defaults if needed
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
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
            "Subsequent log message submitted with invalid severity. Defaulting to info."
        )
        logger.info(msg)
