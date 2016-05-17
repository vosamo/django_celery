from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import tasks
from celery.result import AsyncResult
# Create your views here.

class NewTask(APIView):
    def get(self,request):
        tk = tasks.add.delay(2,3)
        res = 'New task,task id is:%s' % tk.id
        return Response(res, status=status.HTTP_200_OK)

class TaskState(APIView):
    def get(self,request,uuid):
        tk = AsyncResult(uuid)
        if tk.ready():
            res = 'Task result is:%s' % str(tk.get())
        else:
            res = 'Task not finished!'
        return Response(res, status=status.HTTP_200_OK)
