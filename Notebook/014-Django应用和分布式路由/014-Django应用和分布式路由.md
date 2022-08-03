## Django应用和分布式路由

在 Django 中创建应用并在 `settings.py` 文件中注册该应用：



1. 创建应用：

`python manage.py startapp app_name`



2. 注册应用：

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 要注册的应用的路径名字
    # 用 点 表示文件夹的层级关系
    'apps.app_name', 
]
```

















