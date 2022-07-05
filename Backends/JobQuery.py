#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: zhangyuhao
@file: JobQuery.py
@time: 2022/5/29 下午7:35
@email: yuhaozhang76@gmail.com
@desc: 
"""
import pymongo
import json


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["JobInfo"]

mycollect = mydb['jobInfo']

# print(mycollect.find({"tier_first_position":"服务业"}).distinct("jobSalary_format"))
# print(len(mycollect.find({"tier_first_position":"服务业"}).distinct("jobSalary_format")))


def generate_education():
    result = []
    diploma = mycollect.distinct("jobDiploma")
    for single_diploma in diploma:
        number = len(list(mycollect.find({"jobDiploma": single_diploma})))
        result.append({
            "education": single_diploma,
            "num": number
        })

    collections = mydb.list_collection_names()
    if 'education' in collections:
        mydb['education'].drop()
    for item in result:
        mydb.education.insert_one(item)


def generate_map():
    result = []
    province = mycollect.distinct("jobWorkProvince")
    for single_province in province:
        number = len(list(mycollect.find({"jobWorkProvince": single_province})))
        result.append({
            "name": single_province,
            "value": number
        })
    collections = mydb.list_collection_names()
    if 'map' in collections:
        mydb['map'].drop()
    for item in result:
        mydb.map.insert_one(item)


def generate_salary():
    salary_range_list = ["0-5000", "5000-10000", "10000-15000", "15000-20000", "20000+"]
    result = []
    job = mycollect.distinct("tier_first_position")
    for single_job in job:
        salary = {}
        for i, salary_range in enumerate(salary_range_list):
            if i == len(salary_range_list) - 1:
                left_ = int(salary_range[:-1])
                number = len(
                    list(mycollect.find({"tier_first_position": single_job, "jobSalary_format": {'$gte': left_}})))
                salary[salary_range] = number
            else:
                left_ = int(salary_range.split('-')[0])
                right_ = int(salary_range.split('-')[1])
                number = len(list(mycollect.find(
                    {"tier_first_position": single_job, "jobSalary_format": {'$gte': left_, '$lt': right_}})))
                salary[salary_range] = number
        result.append({
            "job": single_job,
            "salary": salary
        })

    collections = mydb.list_collection_names()
    if 'salary' in collections:
        mydb['salary'].drop()
    for item in result:
        mydb.salary.insert_one(item)


if __name__ == '__main__':
    # generate_education()
    generate_map()
    generate_salary()


