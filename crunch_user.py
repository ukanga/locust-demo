# -*- coding=utf-8 -*-
"""
Crunch user locustfile.
"""
import uuid

from locust import HttpLocust, TaskSet


def munch(user):
    """
    Index page.
    """
    user.client.get('/')


def crunch(user):
    """
    Post JSON data to crunch.
    """
    data_str = '{"_id": "locust", "greeting": "Hi"}'
    headers = {'Content-Type': 'application/json'}
    user.client.post('/', headers=headers, data=data_str, name='/crunch')


def crunchy(user):
    """
    Post JSON data to crunch.
    """
    data_str = '{"_id": "%s", "greeting": "Hi"}' % uuid.uuid4()
    headers = {'Content-Type': 'application/json'}
    user.client.post('/', headers=headers, data=data_str)


class CrunchUserBehaviour(TaskSet):
    """
    User behaviour on crunch.
    """
    tasks = {munch: 2, crunch: 1, crunchy: 3}

    def on_start(self):
        """
        on_start is called when a Locust starts before any task is scheduled.
        You can handle use login here.
        """
        pass


class CrunchUser(HttpLocust):  # pylint: disable=R0903
    """
    CrunchUser represents a user/locust.
    """
    task_set = CrunchUserBehaviour
    min_wait = 5000
    max_wait = 9000
