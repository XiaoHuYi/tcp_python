import socket
import time
import struct
import sys
sys.path.append("/home/tcp_python")
from my_tcp.message import Message
from my_tcp.datapack import DataPack

sock = socket.socket()
sock.connect(("127.0.0.1",8800))

while True:
    send_data = b"hello"
    send_data_len = len(send_data)
    send_data_id = 2
    message = Message(send_data,send_data_id)
    # 将message对象进行封包，按照TLV的格式传输 头部包含 正文数据的长度+消息id
    total_send_data = DataPack.pack(message)
    sock.send(total_send_data)
    response = sock.recv(1024)
    print(response)
    time.sleep(1)