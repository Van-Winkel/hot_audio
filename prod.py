import os
import logging
import traceback
from datetime import datetime
from app import tengxun_hot, iqiyi, music_163, qq_music, qq_music_biaosheng, qq_music_liuxingzhishu, qq_music_neidi, qq_music_oumei, qq_music_taiwan, qq_music_tengxunyinyuerenyuanchuang, qq_music_tinggeshiqu, qq_music_xianggang, qq_music_xinge, music_163_biaosheng,music_163_chaoliufengxiang,music_163_oumeirege,music_163_shishiredu,music_163_viprege,music_163_wangluorege,music_163_xinge,music_163_yinyuehehuorenrege,music_163_yuanchuang
from utils import logging, traceback

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_json(json_data, file_name):
    lines = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
    obj = json_data.get("obj", [])

    for item in obj:
        if item["title"] in lines:
            continue
        else:
            with open(file_name, 'a') as fi:
                fi.write(item["title"] + "\n")
    return len(obj)

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def save_data(data, path, filename):
    if data:
        ensure_dir(path)
        file_path = os.path.join(path, filename)
        return fetch_json(data, file_path)
    return 0

def main():
    try:
        if not os.path.exists("status.txt"):
            with open("status.txt", 'a') as fi:
                fi.write("TIME\ttengxun_video\tiqiyi\tqq_music\tqq_music_biaosheng\tqq_music_liuxingzhishu\tqq_music_neidi\tqq_music_oumei\tqq_music_taiwan\tqq_music_tengxunyinyuerenyuanchuang\tqq_music_tinggeshiqu\tqq_music_xianggang\tqq_music_xinge\tmusic_163\tmusic_163_biaosheng\tmusic_163_chaoliufengxiang\tmusic_163_oumeirege\tmusic_163_shishiredu\tmusic_163_viprege\tmusic_163_wangluorege\tmusic_163_xinge\tmusic_163_yinyuehehuorenrege\tmusic_163_yuanchuang\n")

        now = datetime.now()
        hour_file = now.strftime("%Y%m%d%H%M%S")

        # 抓取数据
        tengxun_video_hot = tengxun_hot.tx_hot()
        iqiyi_data = iqiyi.iqiyi()
        qq_music_data = qq_music.qq_music()
        qq_music_biaosheng_data = qq_music_biaosheng.qq_music()
        qq_music_liuxingzhishu_data = qq_music_liuxingzhishu.qq_music()
        qq_music_neidi_data = qq_music_neidi.qq_music()
        qq_music_oumei_data = qq_music_oumei.qq_music()
        qq_music_taiwan_data = qq_music_taiwan.qq_music()
        qq_music_tengxunyinyuerenyuanchuang_data = qq_music_tengxunyinyuerenyuanchuang.qq_music()
        qq_music_tinggeshiqu_data = qq_music_tinggeshiqu.qq_music()
        qq_music_xianggang_data = qq_music_xianggang.qq_music()
        qq_music_xinge_data = qq_music_xinge.qq_music()
        music_163_hot = music_163.music_163()
        music_163_biaosheng_data = music_163_biaosheng.music_163()
        music_163_chaoliufengxiang_data = music_163_chaoliufengxiang.music_163()
        music_163_oumeirege_data = music_163_oumeirege.music_163()
        music_163_shishiredu_data = music_163_shishiredu.music_163()
        music_163_viprege_data = music_163_viprege.music_163()
        music_163_wangluorege_data = music_163_wangluorege.music_163()
        music_163_xinge_data = music_163_xinge.music_163()
        music_163_yinyuehehuorenrege_data = music_163_yinyuehehuorenrege.music_163()
        music_163_yuanchuang_data = music_163_yuanchuang.music_163()


        # 目录定义
        data_sources = {
            "tengxun_video": (tengxun_video_hot, "tengxun_video_records"),
            "iqiyi": (iqiyi_data, "iqiyi_data_records"),
            "qq_music": (qq_music_data, "qq_music_hot_records"),
            "qq_music_biaosheng" : (qq_music_biaosheng_data, "qq_music_biaosheng_records"),
            "qq_music_liuxingzhishu" : (qq_music_liuxingzhishu_data, "qq_music_liuxingzhishu_records"),
            "qq_music_neidi" : (qq_music_neidi_data, "qq_music_neidi_records"),
            "qq_music_oumei" : (qq_music_oumei_data, "qq_music_oumei_records"),
            "qq_music_taiwan" : (qq_music_taiwan_data, "qq_music_taiwan_records"),
            "qq_music_tengxunyinyuerenyuanchuang" : (qq_music_tengxunyinyuerenyuanchuang_data, "qq_music_tengxunyinyuerenyuanchuang_records"),
            "qq_music_tinggeshiqu" : (qq_music_tinggeshiqu_data, "qq_music_tinggeshiqu_records"),
            "qq_music_xianggang" : (qq_music_xianggang_data, "qq_music_xianggang_records"),
            "qq_music_xinge" : (qq_music_xinge_data, "qq_music_xinge_records"),
            "music_163": (music_163_hot, "music_163_hot_records"),
            "music_163_biaosheng": (music_163_biaosheng_data, "music_163_biaosheng_records"),
            "music_163_chaoliufengxiang": (music_163_chaoliufengxiang_data, "music_163_chaoliufengxiang_records"),
            "music_163_oumeirege": (music_163_oumeirege_data, "music_163_oumeirege_records"),
            "music_163_shishiredu": (music_163_shishiredu_data, "music_163_shishiredu_records"),
            "music_163_viprege": (music_163_viprege_data, "music_163_viprege_records"),
            "music_163_wangluorege": (music_163_wangluorege_data, "music_163_wangluorege_records"),
            "music_163_xinge": (music_163_xinge_data, "music_163_xinge_records"),
            "music_163_yinyuehehuorenrege": (music_163_yinyuehehuorenrege_data, "music_163_yinyuehehuorenregerecords"),
            "music_163_yuanchuang": (music_163_yuanchuang_data, "music_163_yuanchuang_records"),
        }

        # 保存数据并统计数量
        counts = {}
        for name, (data, path) in data_sources.items():
            counts[name] = save_data(data, path, f"{hour_file}.lst")

        # 写入状态文件
        with open("status.txt", "a") as status_file:
            status_file.write(
                f"{hour_file}\t{counts['tengxun_video']}\t{counts['iqiyi']}\t"
                f"{counts['qq_music']}\t{counts['qq_music_biaosheng']}\t{counts['qq_music_liuxingzhishu']}\t{counts['qq_music_neidi']}\t{counts['qq_music_oumei']}\t{counts['qq_music_taiwan']}\t{counts['qq_music_tengxunyinyuerenyuanchuang']}\t{counts['qq_music_tinggeshiqu']}\t{counts['qq_music_xianggang']}\t{counts['qq_music_xinge']}\t{counts['music_163']}\t"
                f"{counts['music_163_biaosheng']}\t{counts['music_163_chaoliufengxiang']}\t{counts['music_163_oumeirege']}\t{counts['music_163_shishiredu']}\t{counts['music_163_viprege']}\t{counts['music_163_wangluorege']}\t{counts['music_163_xinge']}\t{counts['music_163_yinyuehehuorenrege']}\t{counts['music_163_yuanchuang']}\n"
            )

        logging.info("Waiting for the next hour...")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        logging.error(traceback.format_exc())

if __name__ == "__main__":
    main()
