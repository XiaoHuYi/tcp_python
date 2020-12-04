

class Message():

    def __init__(self,data=None,id=None) -> None:
        self.data = data
        self.id = id 
        self.data_len = len(self.data)

    def set_data(self,data):
        self.data = data
    
    def set_id(self,id):
        self.id = id

    def get_data(self):
        return self.data

    def get_id(self):
        return self.id
    