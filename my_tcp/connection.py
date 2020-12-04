from .request import Request
from .message import Message
import struct


class Connection():
    def __init__(self,conn,id2route) -> None:
        self.conn = conn
        self.id2route = id2route

    def send_data(self):
        pass

    def handler(self):
        while True:
            try:
                packed_data_len = self.conn.recv(4)
                if not packed_data_len:
                    print('connection lose')
                    break
                data_len = struct.unpack("<i",packed_data_len)[0]
                packed_data_id = self.conn.recv(4)
                data_id = struct.unpack("<i",packed_data_id)[0]
                data  = self.conn.recv(data_len)
                message = Message(data,data_id) # 将接受到的数据封装到一个message对象中
                r = Request(self.conn,message)

                route = self.id2route.get(data_id)
                if not route:
                    print("this message id hasn't resigter router")
                    break

                route.pre_handler(r)
                route.handler(r)
                route.after_handler(r)
                
            except Exception as e:
                print(e)
                break
            

