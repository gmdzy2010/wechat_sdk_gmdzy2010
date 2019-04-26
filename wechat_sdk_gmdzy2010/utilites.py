"""
Toolbox for wechat sdk
"""


def log_wechat_request(cls):
    """Decorator for wechat request class."""
    
    base_classes = cls.__bases__
    origin_getattribute = cls.__getattribute__
    
    def new_getattribute(self, item):
        if hasattr(self, "request_method") and hasattr(self, "request_url"):
            log_info = "%s\t%s" % (self.request_method, self.request_url)
            for base_class in base_classes:
                if item not in base_class.__dict__:
                    self.logger.info(log_info)
        return origin_getattribute(self, item)
    
    # return back to the new magic method: __getattribute__
    cls.__getattribute__ = new_getattribute
    return cls
