

class Request():
    
    def __init__(self,conn,message) -> None:
        self.conn = conn
        self.message = message

    def set_conn(self,conn):
        self.conn = conn

    def set_data(self,data:bytes):
        self.data = data        
    
    def get_conn(self):
        return self.conn

    def get_data(self):
        return self.message.get_data()