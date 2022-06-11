## GET and POST 请求

可以通过视图函数的 request 的属性来获得当前的请求是以什么方式进行的

`request.method` 是请求方式的字符串（大写）

1. 一般来说，获取网页的页面使用 GET 请求
2. 当提交表单的时候使用 POST 请求