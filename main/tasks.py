from __future__ import absolute_import
from time import sleep
from celery import shared_task


@shared_task
def add(x, y):
    sleep(5)
    return x + y


@shared_task
def mul(x, y):
    sleep(5)
    return x * y


@shared_task
def xsum(numbers):
    sleep(5)
    return sum(numbers)
