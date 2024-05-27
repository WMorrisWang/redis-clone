# Redis Clone

This a project aims to learn Redis by recreating a wheel.

## To start the redis server:

```shell
./spawn_redis_server
```

## supported command

### To interact with the redis-clone-server, please install redis-cli

Make a tcp connection and ping for the server health status:

```shell
redis-cli ping -p 6379
```

If you are interested in how I made the decisions in designing this system, please check my [Medium](https://medium.com/@ysheng4g/%E5%BE%9E0%E9%96%8B%E5%A7%8B%E6%89%93%E9%80%A0redis%E4%BC%BA%E6%9C%8D%E5%99%A8%E7%AC%AC1%E7%AF%87-tcp-socket-server-e97e876cdd3d)