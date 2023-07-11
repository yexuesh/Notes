<h1> Mongo <h1/>

<a href="https://pymongo.readthedocs.io/en/stable/api/index.html">API 参考 看这里</a>

### 连接

```python
from pymongo import MongoClient

def getUrl(username, password, ip, port):
	return f"mongodb://{username}:{password}@{ip}:{port}/?directConnection=true&appName=mongosh"

client = MongoClient(uri)
db = client["spider"]
collection = db["Yande"]
```

### 向集合中插入数据

```python
>>> t_data = {
    "url": "https://www.bilibili.com"
}
>>> t_datas = [
    {
        "author": "Mike",
        "text": "Another post!",
        "tags": ["bulk", "insert"],
        "date": datetime.datetime(2009, 11, 12, 11, 14),
    },
    {
        "author": "Eliot",
        "title": "MongoDB is fun",
        "text": "and pretty easy too!",
        "date": datetime.datetime(2009, 11, 10, 10, 45),
    },
]

# 插入单个数据
>>> result_id = collection.insert_one(t_data).inserted_id
>>> type(result_id)
ObjectId("...")
# 批量插入
>>> result_ids = collection.insert_many(t_datas).inserted_ids
[ObjectId("..."), ObjectId("...")]
```

### 查看数据库中的所有集合

```python
>>> db.list_collection_names()
```

### 获取(查询)

高级查询: https://www.mongodb.com/docs/manual/reference/operator/

```python
>>> collection.find_one()  # 单个
>>> for result in collection.find():  # 多个
...     print(result)

>>> collection.count_documents()  # 匹配到的数量
```

