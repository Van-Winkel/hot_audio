import re
import json
import requests
import logging
import traceback


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_url(url, headers=None, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()  # 如果请求失败，抛出异常
            return response  # 返回响应内容
        except requests.RequestException as e:
            logging.error(f"Attempt {attempt + 1} failed: {e}")
    logging.error("All attempts failed.")
