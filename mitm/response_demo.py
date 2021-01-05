from pprint import pprint
from mitmproxy import http

def response(flow: http.HTTPFlow):
    pprint(flow.response.content)
