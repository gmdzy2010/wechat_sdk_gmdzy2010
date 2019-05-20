"""
This module contain the global settings for the python sdk of wechat
"""

import os


# logging setting

LOG_PATH = os.path.dirname(os.path.abspath(__file__))

# The root url of dingtalk api

URL_ROOT = "https://api.weixin.qq.com/"

# The access token should be got from the url below

GLOBAL_ACCESS_TOKEN = URL_ROOT + "cgi-bin/token"

WEB_AUTH_ACCESS_TOKEN = URL_ROOT + "sns/oauth2/access_token"

WEB_AUTH_REFRESH_TOKEN = URL_ROOT + "sns/oauth2/refresh_token"

GET_USERINFO = URL_ROOT + "sns/userinfo"

JS_API_TICKET = URL_ROOT + "cgi-bin/ticket/getticket"
