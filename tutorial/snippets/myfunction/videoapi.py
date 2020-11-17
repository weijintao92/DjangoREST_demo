#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#Date:2020-10
#Author:wjt
#description: 自定义的方法


def get_url_list():
    """
    获取最终的url集合
    """
    with open('./snippets/myfunction/video_result33.txt', "r") as fs:
        os_url = fs.read()
        fs.close()

    return json.loads(os_url)

            