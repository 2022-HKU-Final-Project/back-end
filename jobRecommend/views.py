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
    json_data = json.loads(json_body, encoding='utf-8')
    #get方法键值对方式获取值
    print(json_data)

    key_word = json_data.get('keyword')
    offset = json_data.get('offset')
    if key_word == "":
        print(" no key")
        re = list(mycollect.find({},{"_id": 0}).limit(10).skip(offset))
        
    else:
        job_category_id_list = json_data.get("job_category_id_list")
        if job_category_id_list == []:
            data = {
                'tier_first_position': key_word,
            }
        else:
            data = {
            'tier_first_position': key_word,
            'jobWorkCity_format': {"$in": job_category_id_list},
            
            }
        re = list(mycollect.find(data, {"_id": 0}).limit(10).skip(offset))
    test = {
        'count': 100,
        'city_list': [1,2,3],
        'job_type_list':[1,2,3],
        'job_post_list':re
    }
    print(re)
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
    result = list(mydb['education'].find({}, {"_id": 0}))
    return HttpResponse(json.dumps(result, ensure_ascii=False))


def dashboard_map(request):
    result = list(mydb['map'].find({}, {"_id": 0}))
    for item in result:
        item['name'] = item['name'].strip('省').strip('自治区').strip('市').strip('回族')
    return HttpResponse(json.dumps(result, ensure_ascii=False))


def dashboard_salary(request):
    result = list(mydb['salary'].find({}, {"_id": 0}))
    return HttpResponse(json.dumps(result, ensure_ascii=False))
