import struct

class DataPack():

    @classmethod
    def pack(cls,msg) -> bytes:
        data  = msg.get_data()
        data_len = len(data)
        data_id = msg.get_id()
        pack_len = struct.pack("<i",data_len)
        pack_id = struct.pack("<i",data_id)

        total_data = pack_len + pack_id + data
        return total_data 


