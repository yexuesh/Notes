```python
import pymongo

# 连接Mongo
client = pymongo.MongoClient(host="localhost", port=27017)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# 指定数据库
db = client.test
db = client['test']

# 指定集合
collection = db.students
collection = db['students']

# 插入数据
insert_one(dic)
insert_many([dic1, dic2])
@return: InsertOneResult  --->>   InsertOneResult.insert_id -> @return: _id

# 查询
find_one({"name": "lina"})  @return: dic
results = collection.find({"age": 20})
for result in results:
    print(result)

# 更新
result = collection.update_one()
result = collection.update_many()

condition = {"name": "lina"}
date = collection.find_one(condition)
date["age"] = 16
result = collection.update_one(condition, {"$set": date})
result.matched_count  # 匹配条数
result.modified_count  # 影响的数据条数

# 删除
collection.delete_one({"name": "lina"}) 
collection.delete_many({"age": {"$lt": 25}})


```



