## Ubuntu

### ubuntu安装docker

docker官网有教程

#### 修改源：
```js
vim /etc/docker/daemon.json

{
  "registry-mirrors": ["https://3laho3y3.mirror.aliyuncs.com"]
}

```
#### 重启docker
```
systemctl daemon-reload 
systemctl restart docker
```

#### 查看
```
docker info|grep Mirrors -A 1
```

