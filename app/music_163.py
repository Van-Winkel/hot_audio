from utils import logging, traceback, fetch_url


def music_163():
    try:
        url = "http://kloping.top/api/get/163host"

        response = fetch_url(url)
        if not response:
            raise Exception("Data request failure.")

        response.raise_for_status()  # 检查请求是否成功
        result_map = response.json()
        realtime_list = list(result_map)
        # 遍历结果
        json_response = {
            "code": 200,
            "success": "success",
            "message": "网易云音乐",
            "obj": [],
            # "icon": "https://music.163.com/favicon.ico"  # 32 x 32
        }

        for index, value in enumerate(realtime_list):
            result = {
                "id": index + 1,
                "title": value.get("name") + "\t" + value.get("artist"),
                # "url": f"https://s.weibo.com/weibo?q={value.get('note').replace(' ', '%20')}",
                # "hotValue": value.get("raw_hot")
            }
            json_response["obj"].append(result)

        return json_response
    except Exception as e:
        logging.error(f"Error fetching data from weibo: {e}")
        logging.error(traceback.format_exc())

# # 调用函数并打印结果
# result = weibo()
# print(json.dumps(result, indent=4, ensure_ascii=False))
