from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('hello world')


def index(request):
    content = {
        'name' : "Zhangsan",
        'num_list': [1, 2, 3, 4, 5, 6, 7]
    }

    content['hello'] = 'hello the world'
    content['a'] = 10
    return render(request, 'hello.html', content)


def runboot(request):
    return render(request, 'son_model.html')
