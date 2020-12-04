'''
socket 服务端类
'''
import socket
import gevent
from gevent import monkey
monkey.patch_all()      # 用于将标准库中大部分阻塞式调用修改为协作式运行
from .connection import Connection
from .route import BaseRoute



class  Server():
    def __init__(self,host,port):
        self.port = port
        self.host = host
        self.id2route = {}

    def start(self):
        sock = socket.socket()
        sock.bind((self.host,self.port))
        sock.listen(5)

        while True:
            conn,addr = sock.accept()
            c = Connection(conn,self.id2route)  # 生成一个conn对象
            gevent.spawn(c.handler)  # 生成一个协程让该connection对象去处理连接的业务

    def stop(self):
        pass

    def add_route(self,route):
        self.route = route

    def add_id2route(self,id2route):
        self.id2route = id2route


if __name__ == "__main__":
    s = Server("127.0.0.1",'8800')
    s.start()
