from wechat_sdk_gmdzy2010 import settings
from wechat_sdk_gmdzy2010.base_request import BaseRequest
from wechat_sdk_gmdzy2010.utilites import log_wechat_request


@log_wechat_request
class GlobalAccessTokenRequest(BaseRequest):
    """
    Description: The access token is globally valid within 7200 seconds. To get
    the token, two url parameters are necessary: grant_type, appid and secret,
    by default, those should be contained in your os.environ

    parameter_R: <grant_type>, <appid>, <secret>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: <access_token>, <expires_in>
    """
    request_url = settings.GLOBAL_ACCESS_TOKEN
    
    def get_access_token(self):
        json_response = self.get_json_response()
        if self.call_status:
            access_token = json_response.get("access_token", None)
            return access_token
        return ""


@log_wechat_request
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
        json_response = self.get_json_response()
        if self.call_status:
            access_token = json_response.get("access_token", None)
            return access_token
        return ""
    
    def get_refresh_token(self):
        json_response = self.get_json_response()
        if self.call_status:
            refresh_token = json_response.get("refresh_token", None)
            return refresh_token
        return ""


@log_wechat_request
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
        json_response = self.get_json_response()
        if self.call_status:
            access_token = json_response.get("access_token", None)
            return access_token
        return ""

    def get_refresh_token(self):
        json_response = self.get_json_response()
        if self.call_status:
            refresh_token = json_response.get("refresh_token", None)
            return refresh_token
        return ""
    
    def get_openid(self):
        json_response = self.get_json_response()
        if self.call_status:
            openid = json_response.get("openid", None)
            return openid
        return ""


@log_wechat_request
class UserInfoRequest(BaseRequest):
    """
    parameter_R: <access_token>, <openid>, <lang>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: <access_token>, <expires_in>, <refresh_token>, <openid>, <scope>
    """
    request_url = settings.GET_USERINFO
    
    def get_unionid(self):
        json_response = self.get_json_response()
        if self.call_status:
            unionid = json_response.get("unionid", None)
            return unionid
        return ""
