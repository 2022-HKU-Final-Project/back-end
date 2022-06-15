#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: zhangyuhao
@file: views.py
@time: 2022/6/15 上午11:37
@email: yuhaozhang76@gmail.com
@desc: 
"""
from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect


def index(request):

    return render(request, 'option1/index.html')