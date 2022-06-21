#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: zhangyuhao
@file: JobQuery.py
@time: 2022/5/29 下午7:35
@email: yuhaozhang76@gmail.com
@desc: 
"""
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["route_network"]

mycollect = mydb['route_list']
data = {
    'node': str(origin) + str(dest)
}
re = mycollect.find_one(data)





