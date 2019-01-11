"""
This module contain the global settings for the python sdk of dingtalk
"""


# The root url of dingtalk api

URL_ROOT = "https://api.weixin.qq.com/"

# The access token should be got from the url below

GLOBAL_ACCESS_TOKEN = URL_ROOT + "cgi-bin/token"

WEB_AUTH_ACCESS_TOKEN = URL_ROOT + "sns/oauth2/access_token"

WEB_AUTH_REFRESH_TOKEN = URL_ROOT + "sns/oauth2/refresh_token"

USERINFO = URL_ROOT + "sns/userinfo"