import ahttp

url = "https://www.bilibili.com"
req = ahttp.get(url)  # 构建请求
res = req.run()  # 执行请求
print(res.text)
