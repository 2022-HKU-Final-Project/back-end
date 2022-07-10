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
    job_category_id_list = json_data.get("job_category_id_list")
    location_code_list = json_data.get("location_code_list")
    re = []
    print("job_category_id_list",job_category_id_list)
    print("location_code_list",location_code_list)
    if key_word == "":
        if len(job_category_id_list) == 0:
            if len(location_code_list) == 0:
                re = list(mycollect.find({},{"_id": 0}).limit(10).skip(offset))
            else:
                citie_dic = list(mydb['cityinfo'].find({"code":{"$in": location_code_list}},{"_id": 0,"name":1}))
                cities = []
                for item in citie_dic:
                    cities.append(item['name'])
                re = list(mycollect.find({"jobWorkProvince":{"$in": cities}},{"_id": 0}).limit(10).skip(offset))
        else:
            if len(location_code_list) == 0:
                cats_dic = list(mydb['categories'].find({"id":{"$in": job_category_id_list}},{"_id": 0,"tier_third":1}))
                cats = []
                for item in cats_dic:
                    cats.append(item['tier_third'])
                re = list(mydb['jobinfo'].find({"tier_third_position":{"$in": cats}},{"_id": 0}).limit(10).skip(offset))
            else:
                cats_dic = list(mydb['categories'].find({"id":{"$in": job_category_id_list}},{"_id": 0,"tier_third":1}))
                cats = []
                for item in cats_dic:
                    cats.append(item['tier_third'])
                citie_dic = list(mydb['cityinfo'].find({"code":{"$in": location_code_list}},{"_id": 0,"name":1}))
                cities = []
                for item in citie_dic:
                    cities.append(item['name'])
                print("cats",cats)
                print("cities",cities)
                re = list(mydb['jobinfo'].find({"tier_third_position":{"$in": cats},"jobWorkProvince":{"$in": cities}},{"_id": 0}).limit(10).skip(offset))
                print(re)

       
    else:
        if len(job_category_id_list) == 0:
            if len(location_code_list) == 0:
                re = list(mycollect.find({"$or":[{"tier_first_position":key_word},{"tier_second_position":key_word},{"tier_third_position":key_word}]},{"_id": 0}).limit(10).skip(offset))
                print(re)
            else:
                citie_dic = list(mydb['cityinfo'].find({"code":{"$in": location_code_list}},{"_id": 0,"name":1}))
                cities = []
                for item in citie_dic:
                    cities.append(item['name'])
                re = list(mycollect.find({"jobWorkProvince":{"$in": cities},"$or":[{"tier_first_position":key_word},{"tier_second_position":key_word},{"tier_third_position":key_word}]},{"_id": 0}).limit(10).skip(offset))
        else:
            if len(location_code_list) == 0:
                cats_dic = list(mydb['categories'].find({"id":{"$in": job_category_id_list},},{"_id": 0,"tier_third":1}))
                cats = []
                for item in cats_dic:
                    cats.append(item['tier_third'])
                re = list(mydb['jobinfo'].find({"tier_third_position":{"$in": cats},"$or":[{"tier_first_position":key_word},{"tier_second_position":key_word},{"tier_third_position":key_word}]},{"_id": 0}).limit(10).skip(offset))
            else:
                cats_dic = list(mydb['categories'].find({"id":{"$in": job_category_id_list}},{"_id": 0,"tier_third":1}))
                cats = []
                for item in cats_dic:
                    cats.append(item['tier_third'])
                citie_dic = list(mydb['cityinfo'].find({"code":{"$in": location_code_list}},{"_id": 0,"name":1}))
                cities = []
                for item in citie_dic:
                    cities.append(item['name'])

                re = list(mydb['jobinfo'].find({"tier_third_position":{"$in": cats},"jobWorkProvince":{"$in": cities},"$or":[{"tier_first_position":key_word},{"tier_second_position":key_word},{"tier_third_position":key_word}]},{"_id": 0}).limit(10).skip(offset))
       
    test = {
        'count': 100,
        'city_list': [1,2,3],
        'job_type_list':[1,2,3],
        'job_post_list':re
    }
    return HttpResponse(json.dumps(test, ensure_ascii=False))


def job_filters(request):

    cities = list(mydb['cityinfo'].find({},{"_id": 0}))
    categories = list(mydb['categories'].find({},{"_id": 0,"id":1,"tier_third":1}))
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
