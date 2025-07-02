from utils import logging, traceback, fetch_url


def iqiyi():
    try:
        url = "https://mesh.if.iqiyi.com/portal/lw/search/keywords/hotList?device_id=5434043a6787844d823760badd91f7d0&v=13.062.22175&appMode="

        # 设置请求头
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        }

        # 发送 GET 请求
        response = fetch_url(url, headers=headers)
        if not response:
            raise Exception("Data request failure.")

        response.raise_for_status()  # 检查请求是否成功

        # 解析 JSON 数据
        result_map = response.json()

        # 检查 result_map["data"] 是否存在且类型正确
        if "hotQuery" not in result_map or not result_map["hotQuery"]:
            return {
                "code": 500,
                "message": "API 返回的数据格式不正确"
            }

        data = result_map["hotQuery"]

        # 检查 data 是否为字典类型
        if not isinstance(data, list) or not data:
            return {
                "code": 500,
                "message": "API 返回的 data 字段格式不正确"
            }

        # 检查 data["list"] 是否存在且类型正确
        if "title" not in data[0] or not (data[0]["title"] == '热搜'):
            return {
                "code": 500,
                "message": "API 返回的 list 字段格式不正确"
            }

        list_data = data[0]["items"]

        # 检查 list_data 是否为列表类型
        if not isinstance(list_data, list):
            return {
                "code": 500,
                "message": "API 返回的 list 字段不是数组类型"
            }

        # 构建返回数据
        api = {
            "code": 200,
            "message": "爱奇艺",
            "icon": "https://www.iqiyi.com/favicon.ico",  # 32 x 32
            "obj": []
        }

        for index, item in enumerate(list_data):
            result = {
                "index": index + 1,
                "title": item["title"],
                # "url": f"https://www.bilibili.com/video/{item['bvid']}"
            }
            api["obj"].append(result)

        return api
    except Exception as e:
        logging.error(f"Error fetching data from bilibili: {e}")
        logging.error(traceback.format_exc())

# 测试
# if __name__ == "__main__":
#     result = bilibili()
#     print(json.dumps(result, indent=4, ensure_ascii=False))
