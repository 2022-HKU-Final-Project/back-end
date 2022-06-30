from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from Backends.JobQuery import *
import json
# Create your views here.


def products(request):
    return HttpResponse()


def jobs(request):
    search_key = json.loads(request.body)['keyword']

    # search_key 是 home 搜索内容, 如果为空则说明是首页直接跳转，无输入内容
    print(search_key)

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