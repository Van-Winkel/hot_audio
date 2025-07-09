from utils import logging, traceback, fetch_url
from bs4 import BeautifulSoup


def tx_hot():
    try:
        url = "https://v.qq.com/biu/ranks/?t=hotsearch&channel=0"

        # 设置请求头
        headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
        }

        # 发送 GET 请求
        response = fetch_url(url, headers=headers)
        if not response:
            raise Exception("Data request failure.")

        response.raise_for_status()  # 检查请求是否成功
        response.encoding = 'utf-8'

        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找所有具有 "item item_a" 类的 div 标签
        items = soup.find_all('div', class_='item item_a')

        # 提取每个 div 中 a 标签的 title 属性值
        realtime_list = {item.find('a')['title'] for item in items if item.find('a')}

        # 遍历结果
        json_response = {
            "code": 200,
            "success": "success",
            "message": "腾讯视频",
            "obj": [],
            "icon": "https://v.qq.com/favicon.ico"  # 32 x 32
        }

        for index, value in enumerate(realtime_list):
            result = {
                "id": index + 1,
                "title": value,
                # "url": f"https://s.weibo.com/weibo?q={value.get('note').replace(' ', '%20')}",
                # "hotValue": value.get("raw_hot")
            }
            json_response["obj"].append(result)

        return json_response
    except Exception as e:
        logging.error(f"Error fetching data from weibo: {e}")
        logging.error(traceback.format_exc())
