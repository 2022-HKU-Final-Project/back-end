from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from Backends.JobQuery import *
import json
# Create your views here.


def products(request):
    return HttpResponse()


def jobs(request):

    # search_key 是 home 搜索内容，如果为空则说明是首页直接跳转，无输入内容
    search_key = json.loads(request.body)['keyword']
    print(search_key)

    # job_category_id_list 是 home 下方职位类别跳转，如果为空则说明不是点击下方职位类别跳转，直接忽略
    print(json.loads(request.body)['job_category_id_list'])


    test = {
        'count': 1,
        'city_list': [1,2,3],
        'job_type_list':[1,2,3],
        'job_post_list':[
            {
                "id": 1,
                "title": "测试",
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
        ]
    }
    return HttpResponse(json.dumps(test, ensure_ascii=False))


def jobType(request):
    test = {
        'city_list': [1,2,3],
        'job_type_list':[1,2,3]
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
    data = {
        'jobPosition': list(request.POST.keys())[0]
    }
    re = mycollect.find_one(data)
    print(re)

    return HttpResponse(re)


def job_detail(request, id):
    print(id)
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
    print(request.GET)
    return HttpResponse(json.dumps(test, ensure_ascii=False))