"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from mysite1.views import calculator_view
from mysite1.views import test_request_view
from mysite1.views import test_object_template_view
from mysite1.views import test_template_view
from mysite1.views import test_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # EXAMPLE 1
    # http://127.0.0.1:8000/page/
    # 路由配置项中只需要配置 port/ ... 这里 ... 所表示的内容即可
    # path('page/<int:page_number>/', test_view),

    # EXAMPLE 2
    # 其中 r 代表 raw string, 原始字符串，不经转义的
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})$', calculator_view),

    # EXAMPLE 3
    path('request/', test_request_view),

    path('test-object-template-view/', test_object_template_view),

    path('test-template-view/', test_template_view)
]
