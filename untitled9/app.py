#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-02 11:17
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : app.py
from locust import HttpLocust, TaskSet, task


def index(l):
    l.client.get("/")


def stats(l):
    l.client.get("/stats/requests")


class UserTasks(TaskSet):
    # 列出需要测试的任务形式一
    tasks = [index, stats]

    # 列出需要测试的任务形式二
    @task
    def page404(self):
        self.client.get("/does_not_exist")


class WebsiteUser(HttpLocust):
    host = "http://127.0.0.1:8089"
    min_wait = 2000
    max_wait = 5000
    task_set = UserTasks