## Linux

### 动态查看日志
```sh
tail -200f [log.txt]
```

### 防火墙开放端口
```sh
iptables -I INPUT -p tcp --dport 3000 -j ACCEPT
```

### 安装nodejs/nvm
```sh
sudo curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.2/install.sh | bash^C

source ～/.bashrc
```

### 创建用户与删除用户
- 查看系统所有用户： `/etc/passwd`
- 创建用户 `sudo useradd -m bw30`
- 给用户添加密码 `sudo passwd bw30 123456`
- 给用户添加sodo权限 `sudo usermod -aG sudo username`
- 删除用户 `sudo userdel -r username`
