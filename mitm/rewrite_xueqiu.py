import json
from mitmproxy import http

def response(flow: http.HTTPFlow):
    # 加上过滤条件，x=是接口url地址中的信息，保证修改的是唯一的接口
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 获取response content，使用json，转换文件格式
        data = json.loads(flow.response.content)

        # 修改对应的字段的值
        data['ZH355492']['name'] = "小鱼三高组合小鱼三高组合"
        data['ZH1397286']['name'] = ""

        # 把修改后的数据，转为字符串，赋值给原始响应数据
        flow.response.text = json.dumps(data)

