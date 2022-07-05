from base64 import encode
from curses import keyname
from unicodedata import category
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from Backends.JobQuery import *
import json
import requests
# Create your views here.

model_url = 'http://localhost:8001/get_info'


def products(request):
    data = json.load(open('./Data/data.json', 'r'))['products']
    return HttpResponse(json.dumps(data, ensure_ascii=False))



def jobs(request):
    json_body = request.body
    print(json_body)

    # 把请求体的二进制数据转换为json格式
    json_data = json.loads(json_body)
    #get方法键值对方式获取值

    key_word = json_data.get('keyword')
    offset = json_data.get('offset')
    if key_word == "":
        print(" no key")
        re = list(mycollect.find({},{"_id": 0}).limit(10).skip(offset))
        
    else:
        job_category_id_list = json_data.get("job_category_id_list")
        data = {
            'jobPosition': key_word,
            'jobWorkCity_format':{"$in":job_category_id_list},
            
        }
        re = list(mycollect.find(data,{"_id": 0}).limit(10).skip(offset))
    test = {
        'count': 100,
        'city_list': [1,2,3],
        'job_type_list':[1,2,3],
        'job_post_list':re
    }
    return HttpResponse(json.dumps(test, ensure_ascii=False))


def job_filters(request):

    cities = list(mydb['cityinfo'].find({},{"_id": 0}))
    categories = list(mydb['categories'].find({},{"_id": 0,"tier_first":1}))
    test = {
        'city_list':cities,
        'job_type_list':categories
        }
    return HttpResponse(json.dumps(test, ensure_ascii=False))


def job_categories(request):
    data = json.load(open('./Data/data.json', 'r'))['jobCategories']
    return HttpResponse(json.dumps(data, ensure_ascii=False))


def staff_stories(request):
    data = json.load(open('./Data/data.json', 'r'))['staffStories']
    return HttpResponse(json.dumps(data, ensure_ascii=False))


def byte_standards(request):
    data = json.load(open('./Data/data.json', 'r'))['byteStandards']
    return HttpResponse(json.dumps(data, ensure_ascii=False))


def recommend(request):

    content  = list(request.POST.keys())[0]
    print(content)
    data = {'content':content}
    re = requests.get(model_url, params=data).json()
    print(re['label'])

    return HttpResponse(re['label'])


def job_detail(request, id):
    print(id)
    data = {
        'id': str(id)
    }
    re = mycollect.find_one(data, {"_id": 0})
    return HttpResponse(json.dumps(re, ensure_ascii=False))


def dashboard_education(request):
    result = []
    diploma = mycollect.distinct("jobDiploma")
    for single_diploma in diploma:
        number = len(list(mycollect.find({"jobDiploma": single_diploma})))
        result.append({
            "education": single_diploma,
            "num": number
        })
    return HttpResponse(json.dumps(result, ensure_ascii=False))


def dashboard_map(request):
    result = []
    province = mycollect.distinct("jobWorkProvince")
    for single_province in province:
        number = len(list(mycollect.find({"jobWorkProvince": single_province})))
        result.append({
            "name": single_province,
            "value": number
        })
    return HttpResponse(json.dumps(result, ensure_ascii=False))


def dashboard_salary(request):
    salary_range_list = ["0-5000", "5000-10000", "10000-15000", "15000-20000", "20000+"]
    result = []
    job = mycollect.distinct("tier_first_position")
    for single_job in job:
        salary = {}
        for i, salary_range in enumerate(salary_range_list):
            if i == len(salary_range_list)-1:
                left_ = int(salary_range[:-1])
                number = len(list(mycollect.find({"tier_first_position": single_job, "jobSalary_format": {'$gte': left_}})))
                salary[salary_range] = number
            else:
                left_ = int(salary_range.split('-')[0])
                right_ = int(salary_range.split('-')[1])
                number = len(list(mycollect.find({"tier_first_position": single_job, "jobSalary_format": {'$gte': left_, '$lt': right_}})))
                salary[salary_range] = number
        result.append({
            "job": single_job,
            "salary": salary
        })
    return HttpResponse(json.dumps(result, ensure_ascii=False))