import sys
sys.path.append("/home/tcp_python")

from my_tcp.server import Server
from my_tcp.route import BaseRoute

class Route1(BaseRoute):

    def handler(self,request):
        print("this message id 1")
        conn = request.get_conn()
        data = request.get_data()
        print(data)
        conn.send(data)

    def pre_handler(self,request):
        print("in pre handler")

    def after_handler(self,request):
        print("in after handler")


class Route2(BaseRoute):

    def handler(self,request):
        print("this message id 2")
        conn = request.get_conn()
        data = request.get_data()
        print(data)
        conn.send(data)

    def pre_handler(self,request):
        print("in pre handler")

    def after_handler(self,request):
        print("in after handler")


s = Server("127.0.0.1",8800)
r1 = Route1()
r2 = Route2()

message_id_2_route = {1:r1,2:r2}
id2route = {2:r2,1:r1}
s.add_id2route(id2route)
s.start()