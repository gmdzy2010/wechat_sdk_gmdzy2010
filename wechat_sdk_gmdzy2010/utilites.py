import hashlib
import logging
import os

from wechat_sdk_gmdzy2010.settings import LOG_PATH


def set_logger(level=logging.INFO):
    """Method to build the base logging system. By default, logging level
    is set to INFO."""
    logger = logging.getLogger(__name__)
    logger.setLevel(level=level)
    logger_file = os.path.join(LOG_PATH, 'wechat_sdk.logs')
    logger_handler = logging.FileHandler(logger_file)
    logger_formatter = logging.Formatter(
        '[%(asctime)s | %(levelname)s] %(message)s')
    logger_handler.setFormatter(logger_formatter)
    logger.addHandler(logger_handler)
    return logger


LOGGER = set_logger()


def log_wechat_request(cls):
    """Decorator for wechat request class."""
    
    # TODO: 50% performance loss occurs, this is a critical problem.
    base_classes = cls.__bases__
    origin_getattribute = cls.__getattribute__
    
    def new_getattribute(self, item):
        for base_class in base_classes:
            if item not in base_class.__dict__ and item not in self.__dict__:
                log_info = "{}".format(cls.request_url)
                LOGGER.info(log_info)
        return origin_getattribute(self, item)
    
    # return back to the new magic method: __getattribute__
    cls.__getattribute__ = new_getattribute
    return cls


def generate_querystring(**kwargs):
    params = ["%s=%s" % (k, v) for k, v in kwargs.items()]
    querystring = "&".join(params)
    return querystring


def generate_signature(**kwargs):
    """The method of signature, it takes the sha1 algorithm."""
    params = ["%s=%s" % (k, v) for k, v in sorted(kwargs.items())]
    params_string = "&".join(params)
    params_string_sha1 = hashlib.sha1()
    params_string_sha1.update(params_string.encode("utf8"))
    signature = params_string_sha1.hexdigest()
    return signature
