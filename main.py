# This is a sample Python script.
import argparse
import json
import os
import time
import requests

OPENID = os.getenv("OPENID")


def parse_args():
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--openid', help='输入微信openid')
    args = parser.parse_args()
    return args


'''
返回json示例
{
    "data": [
        {
            "id": 175,
            "name": "学习习近平总书记考察闽江学院重要讲话精神",
            "season_id": 14,
            "period_id": 183,
            "score": 100,
            "type": 0,
            "admin_id": "1",
            "sort": null,
            "study_number": 640729,
            "cover": "",
            "link": "https://h5.cyol.com/special/daxuexi/fu4nh1pd0k/m.html",
            "status": 1,
            "publish_time": "2023-04-10",
            "is_study": 0,
            "created_at": "2023-04-10 10:59:14",
            "updated_at": "2023-04-11 15:11:06"
        }
    ]
}
'''


def get_study_list() -> list:
    url = f"http://qndxx.cqyouths.com/new_course.json?time={int(time.time())}"
    resp = requests.get(url)
    resp_json = json.loads(resp.text)
    return resp_json["data"]


"""
{
    "status": 200,
    "message": "往期课程，不需要学习记录",
    "error": "",
    "data": {
        "id": 17,
        "name": "“青年大学习”第八季第八期",
        "season_id": 2,
        "period_id": 20,
        "score": 0,
        "type": 0,
        "admin_id": "1",
        "sort": null,
        "study_number": 0,
        "cover": "",
        "link": "http:\/\/h5.cyol.com\/special\/daxuexi\/8zspcymlg8\/index.html",
        "status": 1,
        "publish_time": "2020-04-06",
        "is_study": 1,
        "created_at": "2020-09-06 16:58:23",
        "updated_at": "2020-09-06 19:54:16",
        "user_score": 5150
    }
}
"""


# do_study do the real study job
def do_study(course_id) -> str:
    url = f"http://qndxx.cqyouths.com/api/course/studyCourse?openid={OPENID}&id={course_id}"
    resp = requests.get(url)
    resp_json = json.loads(resp.text)
    return resp_json["message"]


# check do_study return result
def check_do_result(study_result: str) -> int:
    if "继续学习" in study_result:
        return 0
    elif "完成" in study_result:
        return 0
    else:
        return 1


if __name__ == '__main__':
    result_int = 0
    conf = parse_args()
    if conf.openid != "":
        OPENID = conf.openid

    study_list = get_study_list()
    for course_info in study_list:
        print(f"开始学习课程：{course_info['name']}, id号：{course_info['id']}")
        result = do_study(course_info["id"])
        print(f"学习结果：{result}")
        if result_int == 0:
            result_int = check_do_result(result)

    exit(result_int)
