from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def test_view(request, page_number):
    html = "<h1>hello world.</h1>"
    return HttpResponse(html)


def calculator_view(request, y, x, op):
    html = "<h1>hello world.</h1>"
    return HttpResponse(html)


def test_request_view(request):
    print("path_info : ", request.path_info)

    return HttpResponse("test_request_view")


def test_object_template_view(request):
    data = {
        'first_value': 111,
        'second_value': 222
    }

    template = loader.get_template('index.html')
    res = template.render(data)  # 通过面向对象的写法对它进行渲染
    # print("res", res)
    return HttpResponse(res)


def test_template_view(request):
    data = {
        'first_value': 111,
        'second_value': 222
    }

    return render(request, 'index.html', data)