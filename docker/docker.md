## docker

### docker安装mysql
```sh
docker pull mysql:5.7:28

docker run -d -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=root mysql:5.7.28

```

### docker安装mongo
```sh
docker pull mongo

# 带密码：
docker run -d -p 27017:27017 --name mongo -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=root mongo

# 无密码：
docker run -d -p 27017:27017 --name mongo  mongo

# 进入容器：
docker exec -it mongo /bin/bash

mongo
use admin
db.auth("用户名 ","密码 ")

```

### docker安装redis
```sh
docker pull redis

docker run -d -p 6379:6379 --name redis redis --requirepass "123456"
```

### docker安装nginx(详见nginx目录)
```sh
# 第一步 把相关的配置都拷贝到本地

docker run -it -p 80:80  -v `pwd`/www:/usr/share/nginx/html -v `pwd`/conf:/etc/nginx  -v `pwd`/logs:/var/log/nginx --name nginx -d  nginx
```
