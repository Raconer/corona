from corona.mapper import auth_mapper
from corona.model.crn_auth import auth
from corona.core import date_util
import os, datetime, time

def is_auth():
    auth_info = auth_mapper.get()
    pid = int(os.getpid())
    if auth_info is None:
        auth_data = auth()
        auth_data.pid = pid
        auth_data.regDate = date_util.get_kst()
        
        auth_mapper.insert(auth_data)
        time.sleep(1)
        auth_info = auth_mapper.get()

    if auth_info.pid == pid:
        return True
    else:
        return False