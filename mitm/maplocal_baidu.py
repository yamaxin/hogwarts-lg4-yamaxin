from mitmproxy import http

# request方法名不可以被修改
def request(flow: http.HTTPFlow):
    # 发起请求，判断url是不是预期的url
    if flow.request.pretty_url == "https://www.baidu.com/":
        # 如果是，创造一个预期的response
        # make方法指定返回的状态码，指定返回内容，指定头信息Content-Type
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            b"Hello World",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )