from utils import logging, traceback, fetch_url


def qq_music():
    try:
        url = "https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?type=top&topid=26&tpl=3"

        response = fetch_url(url)
        if not response:
            raise Exception("Data request failure.")

        response.raise_for_status()  # 检查请求是否成功
        result_map = response.json()

        realtime_list = result_map.get("songlist", [])

        # 遍历结果
        json_response = {
            "code": 200,
            "success": "success",
            "message": "qq音乐-热歌榜",
            "obj": [],
            "icon": "https://c.y.qq.com/favicon.ico"  # 32 x 32
        }

        for index, value in enumerate(realtime_list):
            item_data = value.get("data", {})
            singer = item_data.get("singer", [])
            singer_name = ""
            if singer:
                singer_name = "/".join([item.get("name", "") for item in singer])
            result = {
                "id": index + 1,
                "title": item_data.get("songname", "") + "\t" + singer_name,
                # "url": f"https://s.weibo.com/weibo?q={value.get('note').replace(' ', '%20')}",
                "hotValue": value.get("raw_hot")
            }
            json_response["obj"].append(result)

        return json_response
    except Exception as e:
        logging.error(f"Error fetching data from weibo: {e}")
        logging.error(traceback.format_exc())

