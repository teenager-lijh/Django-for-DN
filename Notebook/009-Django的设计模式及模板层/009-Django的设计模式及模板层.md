## Django 的设计模式及模板层

传统的 MVC :

![image-20220610212710624](009-Django%E7%9A%84%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F%E5%8F%8A%E6%A8%A1%E6%9D%BF%E5%B1%82.assets/image-20220610212710624.png)



1. Model 和 View 服务于 Controller 层
2. Controller 负责主要的业务逻辑，调用 Model 查询数据库，调用 View 渲染 HTML 页面，最后由 Controller 返回最终的页面到 Web 浏览器



Django 的 MTV 设计模式：

![image-20220610213227191](009-Django%E7%9A%84%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F%E5%8F%8A%E6%A8%A1%E6%9D%BF%E5%B1%82.assets/image-20220610213227191.png)

1. Model 和 Template 服务于 View 层
2. Template 负责渲染页面，Model 负责访问数据库，两者可被 View 调用，最终数据由 View 返回到 Web 浏览器
3. Django 中的主路由就相当于 MVC 中的 Controller 
4. 在原 MVC 设计模式中的 V 被拆成了 MTV 中的 T 和 V

所有的设计模式的名字都不重要，重要的是用更合理的方式来解决问题



## 模板层的配置

在 settings.py 中的 TEMPLATES 配置和模板相关的内容：

1. BACKEND : 指定模板的引擎
2. DIRS : 模板的搜素目录
3. APP_DIRS : 是否要在应用中 templates 文件夹中搜索模板文件
4. POTIONS : 有关模板的选项



## 配置中的配置项

DIRS ==> 

`'DIRS':[os.path.join(BASE_DIR, 'templates')]`





## 关于模板

关于模板：模板文件也是一个普通的 html 文件，只不过这个文件会拿给 Django 进行二次处理后才会返回给最终的浏览器

### 模板加载方法 1

`from django.template import loader`

1. 通过 loader 加载模板

​	`template = loader.get_template("template_name")`

2. 将模板文件渲染为最终的 HTML

​	`html = template.render(dict_data)`

3. 用 HttpResponse 将数据返回给浏览器

​	`return HttpResponse(html)`

例如上述代码中的 dict_data 的内容如下：

```python
    dict_data = {
        'first_value': 111,
        'second_value': 222
    }
```

那么在模板 html 文件中可以通过双花括号的方式来引用 `dict_data` 中的值，如：`{{ first_value }}` `{{ second_value }}`

在模板 html 中使用这样的写法，可以将上边双花括号这个整体替换成字典中的值。替换的过程就是通过这行代码来完成的，这个过程也叫做渲染 (render):

​	`html = template.render(dict_data)`

## 模板加载方法 2

使用单独的模板渲染函数来完成

`from django.shortcuts import render`

在视图函数中直接返回 render 函数 的处理结果即可

dict_data 是可选的

`return render(request, 'template_name', dict_data)`



## 总结

1. 在 settings.py 中配置模板层
2. 加载模板并渲染的两种方式
3. 在视图函数中传递数据给模板，其实只是在用 render 函数对已经写好的 html 模板做一个修改和填充而已
4. Django 的 MTV 设计模式