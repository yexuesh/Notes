# urllib.parse

## url解析

```
urlparse(url : str)
# 解析出 协议，域名，...
```



## 合并url

```python
urljoin(Base_url, Append_url)
urljoin("https://baidu.com", "a.html")  # 合并url
```

## 将字典转化为url参数

```python
params = {
    "name": "lina",
    "age": 12
}
base_url = "https://www.baidu.com"
url = base_url + urlencode(params)  # 将字典转化为url参数
```

## 将get请求参数转化为字典

```python
url_get_params = "name=lina&age=12"
params = parse_qs(url_get_params)  # 将get请求参数转化为字典
```

## 将内容转化为url编码

```python
keyword = "汉字"
quote(keyword)  # 将内容转化为url编码(一般参数包含中文时使用)
```

## url解码(对应于↑)

```python
unquote()  # url解码(对应于↑)
```

