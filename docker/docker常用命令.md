## docker 常用命令

### 进入到docker容器
- 但是它有一个缺点，只要这个连接终止，或者使用了exit命令，容器就会退出后台运行
```sh
docker attach db3 
# 或者 
docker attach d48b21a7e439
```
- `docker exec` 这个命令使用exit命令后，不会退出后台，一般使用这个命令
```sh
docker exec -it db3 /bin/sh 或者 docker exec -it d48b21a7e439 /bin/sh
```

### docker提交新的镜像
```sh
docker commit afcaf46e8305(容器id) xwiki-dev（自定义名）
```

### 删除镜像
```sh
docker rmi <image id>
```

### docker查看容器的日记
```sh
docker logs -f -t --tail 100 [容器名/id]
```

### docker进入到一个正在运行的容器内
```sh
docker exec -it [容器id] /bin/sh
```
