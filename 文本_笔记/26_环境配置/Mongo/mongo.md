### 开放防火墙27017

```sh
iptables -A INPUT -p tcp -m state --state NEW -m tcp --dport 27017 -j ACCEPT
```

### 用户管理

role里的角色可以选：

Built-In Roles（内置角色分类）：

- 数据库用户角色：read、readWrite;
- 数据库管理角色：dbAdmin、dbOwner、userAdmin；
- 集群管理角色：clusterAdmin、clusterManager、clusterMonitor、hostManager；
- 备份恢复角色：backup、restore；
- 所有数据库角色：readAnyDatabase、readWriteAnyDatabase、userAdminAnyDatabase、dbAdminAnyDatabase
- 超级用户角色：root
  // 这里还有几个角色间接或直接提供了系统超级用户的访问（dbOwner 、userAdmin、userAdminAnyDatabase）
- 内部角色：__system

每个角色的功能：

- Read：允许用户读取指定数据库
- readWrite：允许用户读写指定数据库
- dbAdmin：允许用户在指定数据库中执行管理函数，如索引创建、删除，查看统计或访问system.profile
- userAdmin：允许用户向system.users集合写入，可以找指定数据库里创建、删除和管理用户
- clusterAdmin：只在admin数据库中可用，赋予用户所有分片和复制集相关函数的管理权限。
- readAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的读权限
- readWriteAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的读写权限
- userAdminAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的userAdmin权限
- dbAdminAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的dbAdmin权限。
- root：只在admin数据库中可用。超级账号，超级权限。

```sh
# 一般规则
{
  user: "<name>",
  pwd: "<cleartext password>",
  # 配置用户拥有的角色列表
  roles: [
    { role: "<role>", db: "<database>" } | "<role>",
    ...
  ],
  authenticationRestrictions: [
     {
      // 配置可允许连接的客户端白名单
       clientSource: ["<IP>" | "<CIDR range>", ...],
       // 配置可连接的服务端白名单
       serverAddress: ["<IP>" | "<CIDR range>", ...]
     },
     ...
  ]
}

# root
db.createUser({
	user:"root",
	pwd:"root",
	roles:[{role:"root","db":"admin"]},
	authenticationRestrictions:[{clientSource:["127.0.0.1"]}]
})

# admin
db.createUser({
	user: 'myadmin',
	pwd: 'myadmin',
    roles:["dbAdminAnyDatabase", "readWriteAnyDatabase"]
})

# 修改
db.update("myadmin", {pwd: 'myadmin123', roles:["dbAdminAnyDatabase", "readWriteAnyDatabase"]}

# 其他commend
use <username>  # 切换用户
show users  # 列出所有用户
```

### 配置文件路径

```sh
sudo vim /etc/mongod.conf
```

```yaml
net:
  port: 27017
  bindIp: 0.0.0.0

security:
  authorization: enabled
```

```sh
# 重启服务
net restart MongoDB

# 停止服务
net stop MongoDB

# 启动服务
net start MongoDB
```

