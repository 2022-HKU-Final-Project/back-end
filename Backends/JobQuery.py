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
import sys
from tqdm import tqdm
import json
from Backends.generateJobInfo import *


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["JobInfo"]

mycollect = mydb['jobinfo']

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
    job = mycollect.distinct("tier_first_position")
    province = mycollect.distinct("jobWorkProvince")
    print(job)
    print(province)
    for single_job in tqdm(job):
        province_info = {}
        for single_province in province:
            number = len(list(mycollect.find({"jobWorkProvince": single_province, "tier_first_position": single_job})))
            province_info[single_province] = number
        result.append({
            "job": single_job,
            "city": province_info
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


def generate_job_count():
    jobs = mycollect.distinct("tier_first_position")
    result = []
    for single_job in tqdm(jobs, desc="handling"):
        count = len(list(mycollect.find({"tier_first_position": single_job})))
        result.append({
            "name": single_job,
            "value": count
        })
    collections = mydb.list_collection_names()
    if 'jobCount' in collections:
        mydb['jobCount'].drop()
    for item in result:
        mydb.jobCount.insert_one(item)


def generate_job_diploma():
    jobs = mycollect.distinct("tier_first_position")
    diploma = mycollect.distinct("jobDiploma")
    result = []
    for single_job in tqdm(jobs, desc="handling"):
        temp_diploma = []
        for single_diploma in diploma:
            temp_re = list(mycollect.find({"tier_first_position": single_job, "jobDiploma": single_diploma}))
            for item in temp_re:
                temp_diploma.append({
                    single_diploma: item['jobSalary_format']
                })

        result.append({
            "name": single_job,
            "data": temp_diploma
        })
    collections = mydb.list_collection_names()
    if 'jobDiploma' in collections:
        mydb['jobDiploma'].drop()
    for item in result:
        mydb.jobDiploma.insert_one(item)


def handle_new_data(job_title, raw_data_path, save_path):

    df_data = generate_final_data(job_title, raw_data_path, save_path)
    processed_json = json.loads(df_data.T.to_json()).values()
    mycollect.insert_many(processed_json)


if __name__ == '__main__':
    # generate_education()
    # generate_map()
    # generate_salary()
    # generate_job_count()
    # generate_job_diploma()
    save_file_path = './final_data.csv'
    job_title_info = './new_tier1-tier2-tier3.csv'
    raw_data = './all_data.csv'
    handle_new_data(job_title_info, raw_data, save_file_path)


