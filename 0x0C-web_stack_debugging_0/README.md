# 0x0C. Web stack debugging #0
![debug_illustration](https://cdn.lynda.com/course/645067/645067-636614622227054107-16x9.jpg)

Debug Apach server to display line of text

### Start

```
root@vagrant-ubuntu-trusty-64:/home/vagrant# docker run -p 8080:80 -d -it holbertonschool/265-0
d275ce8cffc10fa1fab33f6d61d40b6530e3693c7bf097128be6d51ac63c0fda
root@vagrant-ubuntu-trusty-64:/home/vagrant# docker ps
CONTAINER ID        IMAGE                          COMMAND             CREATED             STATUS              PORTS                  NAMES
d275ce8cffc1        holbertonschool/265-0:latest   "/bin/bash"         2 seconds ago       Up 1 seconds        0.0.0.0:8080->80/tcp   high_euclid
root@vagrant-ubuntu-trusty-64:/home/vagrant# curl 0:8080
curl: (56) Recv failure: Connection reset by peer
root@vagrant-ubuntu-trusty-64:/home/vagrant
```

### Finish

```
root@vagrant-ubuntu-trusty-64:/home/vagrant# curl 0:8080
Hello Holberton
root@vagrant-ubuntu-trusty-64:/home/vagrant#
```
