#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: zhangyuhao
@file: scheduleTask.py
@time: 2022/7/18 上午10:57
@email: yuhaozhang76@gmail.com
@desc: 
"""
from apscheduler.schedulers.blocking import BlockingScheduler
from Backends.JobQuery import *


def scheduler_monitor():
    scheduler_task = BlockingScheduler()
    scheduler_task.add_job(generate_map, 'interval', days=7, id='test_job1')
    scheduler_task.add_job(generate_salary, 'interval', days=7, id='test_job1')
    scheduler_task.add_job(generate_job_count, 'interval', days=7, id='test_job1')
    scheduler_task.add_job(generate_job_diploma, 'interval', days=7, id='test_job1')
    scheduler_task.start()


if __name__ == '__main__':
    scheduler_monitor()