from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from Backends.JobQuery import *
import json
# Create your views here.


def products(request):
    return HttpResponse()


def jobList(request):
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