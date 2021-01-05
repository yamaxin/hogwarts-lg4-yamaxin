from mitmproxy import http

def request(flow: http.HTTPFlow):
    flow.request.headers["myheader"] = "anan"
    print(flow.request.headers)