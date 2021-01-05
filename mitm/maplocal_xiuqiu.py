from mitmproxy import http

# request方法名不可以被修改
def request(flow: http.HTTPFlow):
    # 发起请求，判断接口中是否包含quote.json
    if "quote.json" in flow.request.pretty_url:
        # 打开一个保存在本地的数据文件
        with open ("/Users/yamaxin/mitm/quote.json") as f:
            # make方法指定返回数据
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                # 读取文件数据作为返回内容
                f.read(),
                # 头信息是json格式
                {"Content-Type": "application/json"}  # (optional) headers
            )