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
    test = {
        "job_post_detail": {
            "id": 1,
            "city_info": {
                "name": "南京"
            },
            "job_category": {
                "name": "程序猿"
            },
            "recruit_type": {
                "name": "正式"
            },
            "description": "testtesttesttesttesttesttesttesttesttest",
            "requirement": "testtesttesttesttesttesttesttesttesttest"
        }
    }
    print(re)
    return HttpResponse(json.dumps(re, ensure_ascii=False))


def dashboard_education(request):
    test = [
        {
          "education": "学历不限",
          "num": 2000

        },
        {
          "education": "初中及以下",
          "num": 3028
        },
        {
          "education": "中专及以下",
          "num": 567
        },
        {
          "education": "中专/中技",
          "num": 2000
        },
        {
          "education": "高中",
          "num": 2000

        }]

    return HttpResponse(json.dumps(test, ensure_ascii=False))


def dashboard_map(request):
    test = [
        {
          "name": "北京",
          "value": 540
        },
        {
          "name": "天津",
          "value": 130
        }]

    return HttpResponse(json.dumps(test, ensure_ascii=False))


def dashboard_salary(request):
    test = [
        {
          "job": "后端开发",
          "salary": {
              "1000-2000": 5,
              "2000-3000": 4
          }
        },
        {
          "job": "初中及以下",
          "salary": {
              "1000-2000": 5,
              "2000-3000": 4
          }
        },
        {
          "job": "中专及以下",
          "salary": {
              "1000-2000": 5,
              "2000-3000": 4
          }
        },
        {
          "job": "中专/中技",
          "salary": {
              "1000-2000": 5,
              "2000-3000": 4
          }
        },
        {
          "job": "高中",
          "salary": {
              "1000-2000": 5,
              "2000-3000": 4
          }

        }]

    return HttpResponse(json.dumps(test, ensure_ascii=False))