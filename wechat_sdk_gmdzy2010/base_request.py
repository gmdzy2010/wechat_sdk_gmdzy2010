import logging
import os
import requests


class BaseRequest(object):
    """The base request for wechat"""
    logs_path = os.path.dirname(os.path.abspath(__file__))
    request_url = None
    request_methods_valid = [
        "get", "post", "put", "delete", "head", "options", "patch"
    ]
    
    def __new__(cls, cls_name, bases, attrs):
        
        # Ensure initialization is only performed for subclasses of BaseRequest
        parents = [b for b in bases if isinstance(b, BaseRequest)]
        if not parents:
            return super().__new__(cls, cls_name, bases, attrs)

    
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.logger = self.set_logger()
        self.response = None
        self.json_response = None
        self.call_status = False
        self.error_code = None
        self.error_message = None
        self._request_method = "get"
    
    def set_logger(self):
        """Method to build the base logging system. By default, logging level
        is set to INFO."""
        logger = logging.getLogger(__name__)
        logger.setLevel(level=logging.INFO)
        logger_file = os.path.join(self.logs_path, 'wechat_sdk.logs')
        logger_handler = logging.FileHandler(logger_file)
        logger_formatter = logging.Formatter(
            '[%(asctime)s | %(levelname)s] %(message)s')
        logger_handler.setFormatter(logger_formatter)
        logger.addHandler(logger_handler)
        return logger
    
    @property
    def request_method(self):
        """Mostly, the get method is used to request wanted json data, as a
        result, the property of request_method is set to get by default."""
        return self._request_method
    
    @request_method.setter
    def request_method(self, method_str):
        request_method_lower = method_str.lower()
        if request_method_lower in self.request_methods_valid:
            self._request_method = request_method_lower
        else:
            raise ValueError(
                "%s is not a valid HTTP request method, please choose one"
                "of [%s] to perform a normal http request, correct it now."
                "" % (method_str, ", ".join(self.request_methods_valid)))
    
    def get_response(self, encoding="utf-8"):
        """Get the original response of requests"""
        request = getattr(requests, self.request_method, None)
        request.encoding = encoding
        if request is None and self._request_method is None:
            raise ValueError("A effective http request method must be set")
        if self.request_url is None:
            raise ValueError(
                "Fatal error occurred, the class property \"request_url\" is"
                "set to None, reset it with an effective url of wechat api.")
        response = request(self.request_url, **self.kwargs)
        self.response = response
        return response
    
    def get_json_response(self, encoding="utf-8"):
        """This method aims at catching the exception of ValueError, detail:
        http://docs.python-requests.org/zh_CN/latest/user/quickstart.html#json
        """
        self.json_response = self.get_response(encoding=encoding).json()
        if "errcode" in self.json_response and "errmsg" in self.json_response:
            self.error_code = self.json_response["errcode"]
            self.error_message = self.json_response["errmsg"]
        else:
            self.call_status = True
        return self.json_response
    
    def get_call_status(self):
        """The global status of api calling."""
        return self.call_status
