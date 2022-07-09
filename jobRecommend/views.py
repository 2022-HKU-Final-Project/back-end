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

    # 把请求体的二进制数据转换为json格式
    json_data = json.loads(json_body)
    #get方法键值对方式获取值

    key_word = json_data.get('keyword')
    offset = json_data.get('offset')
    if key_word == "":
        print("no key")
        re = list(mycollect.find({},{"_id": 0}).limit(10).skip(offset))
        
    else:
        job_category_id_list = json_data.get("job_category_id_list")
        print(job_category_id_list)
        jobs = list(mycollect['categories'].find({"id":{"$in": job_category_id_list}},{"_id": 0,"tier_third":1}))
        print("jobs2",jobs)
        # print(job_category_id_list)
        if job_category_id_list == []:
            data = {
                'tier_first_position': key_word,
            }
        else:
            data = {
            'tier_first_position': key_word,
            'jobWorkCity_format': {"$in": job_category_id_list}

            }
        re = list(mycollect.find({"$or":[data,{'tier_second_position': key_word,
            'jobWorkCity_format': {"$in": job_category_id_list}},
            {'tier_third_position': key_word,
            'jobWorkCity_format': {"$in": job_category_id_list}}]}, {"_id": 0}).limit(10).skip(offset))
    test = {
        'count': 100,
        'city_list': [1,2,3],
        'job_type_list':[1,2,3],
        'job_post_list':re
    }
    # print(re)
    return HttpResponse(json.dumps(test, ensure_ascii=False))


def job_filters(request):

    cities = list(mydb['cityinfo'].find({},{"_id": 0}))
    categories = list(mydb['categories'].find({},{"_id": 0,"id":1,"tier_third":1}))
    # print(categories)
    test = {
        'city_list':cities,
        'job_type_list':categories
        }
    return HttpResponse(json.dumps(test, ensure_ascii=False))


def job_categories(request):
    data = json.load(open('./Data/data.json', 'r'))['jobCategories']
    job = mydb['categories'].find({},{"_id": 0,"id":1,"tier_third":1})
    result = []
    count = 0
    for single_job in job:
        if count == 7:
            break
        result.append({
            "id": single_job["id"],
            "en_name": "test",
            "zh_name": single_job["tier_third"],
            "image": data[(count % len(data))]['image']
        })
        count += 1
    result.append({
        "id": -1,
        "en_name": "test",
        "zh_name": "全部",
        "image": data[(count % len(data))]['image']
    })

    return HttpResponse(json.dumps(result, ensure_ascii=False))


def staff_stories(request):
    data = json.load(open('./Data/data.json', 'r'))['staffStories']
    return HttpResponse(json.dumps(data, ensure_ascii=False))


def byte_standards(request):
    data = json.load(open('./Data/data.json', 'r'))['byteStandards']
    return HttpResponse(json.dumps(data, ensure_ascii=False))


def recommend(request):

    content = list(request.POST.keys())[0]
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
    new_result = []
    for item in result:
        temp_dict = {'job': item['job'], 'city': []}
        for province in item['city']:
            new_province = province.strip('省').strip('自治区').strip('市').strip('回族')
            temp_dict['city'].append({new_province: item['city'][province]})
        new_result.append(temp_dict)

    return HttpResponse(json.dumps(new_result, ensure_ascii=False))


def dashboard_salary(request):
    result = list(mydb['salary'].find({}, {"_id": 0}))
    return HttpResponse(json.dumps(result, ensure_ascii=False))
