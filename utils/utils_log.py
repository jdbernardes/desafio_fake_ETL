from functools import wraps

from loguru import logger

logger.remove()
log = "./logs/etl.log"
logger.add(log, format="{time} {level} {message} {file}", level="INFO")


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(
            f"""Calling function "{func.__name__}", with args {args}
                    and kwargs {kwargs}"""
        )
        try:
            result = func(*args, **kwargs)
            logger.info(f'Function "{func.__name__}" returned {result}.')
            return result
        except Exception as e:
            logger.exception(f"Error logged in {func.__name__}: {e}")
            raise

    return wrapper
