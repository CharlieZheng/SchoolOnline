(链接)[http://www.cnblogs.com/derek1184405959/p/8590360.html]
 - Ubuntu安装Pillow
```sudo apt-get install python-imaging```

#### MySQL数据库的字符修改

```
sudo vi /etc/mysql/my.cnf
```

新增一下内容
```
[client]
default-character-set=utf8
[mysqld]
character-set-server=utf8
collation-server=utf8_general_ci
```

重启服务
```sudo /etc/init.d/mysql restart```

再次查看字符集
```show variables like '%char%';```