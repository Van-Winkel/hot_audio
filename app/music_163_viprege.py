from utils import logging, traceback, fetch_url
from bs4 import BeautifulSoup
import json


def music_163():
    try:
        url = "https://music.163.com/discover/toplist?id=7785066739"

        # 设置请求头
        headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'priority': 'u=0, i',
        'referer': 'https://music.163.com/',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
        }

        # 发送 GET 请求
        response = fetch_url(url, headers=headers)
        if not response:
            raise Exception("Data request failure.")

        response.raise_for_status()  # 检查请求是否成功
        soup = BeautifulSoup(response.text, 'html.parser')

        # 获取 textarea 内容
        data = soup.find("textarea", {"id": "song-list-pre-data"}).text
        realtime_list = json.loads(data)
        json_response = {
            "code": 200,
            "success": "success",
            "message": "网易云音乐-黑胶VIP热歌榜",
            "obj": [],
            "icon": "https://c.y.qq.com/favicon.ico"  # 32 x 32
        }

        for index, value in enumerate(realtime_list):
            singer = value.get("artists", [])
            singer_name = ""
            if singer:
                singer_name = "/".join([item.get("name", "") for item in singer])
            result = {
                "id": index + 1,
                "title": value.get("name", "") + "\t" + singer_name,
                # "url": f"https://s.weibo.com/weibo?q={value.get('note').replace(' ', '%20')}",
            }
            json_response["obj"].append(result)

        return json_response
    except Exception as e:
        logging.error(f"Error fetching data from weibo: {e}")
        logging.error(traceback.format_exc())


