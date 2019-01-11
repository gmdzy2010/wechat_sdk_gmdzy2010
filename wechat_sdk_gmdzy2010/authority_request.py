from wechat_sdk_gmdzy2010.base_request import BaseRequest
from wechat_sdk_gmdzy2010 import settings


class GlobalAccessTokenRequest(BaseRequest):
    """
    Description: The access token is globally valid within 7200 seconds. To get
    the token, two url parameters are necessary: grant_type, appid and secret,
    by default, those should be contained in your os.environ

    parameter_R: <grant_type>, <appid>, <secret>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: <access_token>, <expires_in>,
    """
    request_url = settings.GLOBAL_ACCESS_TOKEN
    
    def get_access_token(self):
        access_token = self.json_response.get("access_token", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return access_token


class WebAuthorizationAccessTokenRequest(BaseRequest):
    """
    Description: The access token is globally valid within 7200 seconds. To get
    the token, two url parameters are necessary: grant_type, appid and secret,
    by default, those should be contained in your os.environ

    parameter_R: <appid>, <secret>, <code>, <grant_type>,
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: <access_token>, <expires_in>, <refresh_token>, <openid>, <scope>
    """
    request_url = settings.WEB_AUTH_ACCESS_TOKEN
    
    def get_access_token(self):
        access_token = self.json_response.get("access_token", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return access_token

    def get_refresh_token(self):
        access_token = self.json_response.get("refresh_token", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return access_token


class WebAuthorizationRefreshTokenRequest(BaseRequest):
    """
    Description: The access token is globally valid within 7200 seconds. To get
    the token, two url parameters are necessary: grant_type, appid and secret,
    by default, those should be contained in your os.environ

    parameter_R: <appid>, <grant_type>, <refresh_token>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: <access_token>, <expires_in>, <refresh_token>, <openid>, <scope>
    """
    request_url = settings.WEB_AUTH_ACCESS_TOKEN
    
    def get_access_token(self):
        access_token = self.json_response.get("access_token", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return access_token

    def get_refresh_token(self):
        access_token = self.json_response.get("refresh_token", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return access_token


class UserInfoRequest(BaseRequest):
    """
    parameter_R: <appid>, <grant_type>, <refresh_token>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: <access_token>, <expires_in>, <refresh_token>, <openid>, <scope>
    """
    request_url = settings.USERINFO
    
    def get_openid(self):
        openid = self.json_response.get("openid", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return openid

    def get_unionid(self):
        unionid = self.json_response.get("unionid", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return unionid
