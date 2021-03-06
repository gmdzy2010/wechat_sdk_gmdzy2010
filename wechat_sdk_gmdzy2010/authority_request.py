from wechat_sdk_gmdzy2010 import settings
from wechat_sdk_gmdzy2010.base_request import BaseRequest


class GlobalAccessTokenRequest(BaseRequest):
    """
    Description: The access token is globally valid within 7200 seconds.
    While three are 3 required parameters: grant_type, appid and secret,
    secret should be stored in your os.environ.
    
    parameter_R: <grant_type>, <appid>, <secret>
    parameter_O: None
    
    post_data_R: None
    post_data_O: None
    
    Return: <access_token>, <expires_in>
    """
    request_url = settings.GLOBAL_ACCESS_TOKEN
    
    def get_access_token(self):
        if self.call_status:
            access_token = self.json_response.get("access_token", None)
            return access_token
        return ""


class WebAuthorizationAccessTokenRequest(BaseRequest):
    """
    Description: This token request is just for the oauth.
    
    parameter_R: <appid>, <secret>, <code>, <grant_type>,
    parameter_O: None
    
    post_data_R: None
    post_data_O: None
    
    Return: <access_token>, <expires_in>, <refresh_token>, <openid>, <scope>
    """
    request_url = settings.WEB_AUTH_ACCESS_TOKEN
    
    def get_access_token(self):
        if self.call_status:
            access_token = self.json_response.get("access_token", None)
            return access_token
        return ""
    
    def get_refresh_token(self):
        if self.call_status:
            refresh_token = self.json_response.get("refresh_token", None)
            return refresh_token
        return ""

    def get_openid(self):
        if self.call_status:
            openid = self.json_response.get("openid", None)
            return openid
        return ""


class WebAuthorizationRefreshTokenRequest(BaseRequest):
    """
    Description: Request for refreshing token.

    parameter_R: <appid>, <grant_type>, <refresh_token>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: <access_token>, <expires_in>, <refresh_token>, <openid>, <scope>
    """
    request_url = settings.WEB_AUTH_ACCESS_TOKEN
    
    def get_access_token(self):
        if self.call_status:
            access_token = self.json_response.get("access_token", None)
            return access_token
        return ""

    def get_refresh_token(self):
        if self.call_status:
            refresh_token = self.json_response.get("refresh_token", None)
            return refresh_token
        return ""


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
        if self.call_status:
            unionid = self.json_response.get("unionid", None)
            return unionid
        return ""


class JsApiTicketRequest(BaseRequest):
    """
    parameter_R: <access_token>, <type>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: <errcode>, <errmsg>, <ticket>, <expires_in>
    """
    request_url = settings.JS_API_TICKET
    
    def get_ticket(self):
        if self.call_status:
            ticket = self.json_response.get("ticket", None)
            return ticket
        return ""
