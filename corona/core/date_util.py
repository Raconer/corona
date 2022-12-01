import datetime
from pytz import timezone, utc
from corona.core import text_format
from corona.mapper import local_mapper
from corona.service import set_service

def get_kst():
    KST = datetime.datetime.now(timezone('Asia/Seoul'))
    return KST.strftime(text_format.date_format1)

def get_add_day():
    cur_date = datetime.datetime.strptime(get_kst(), text_format.date_format1)
    cur_date_s = cur_date.strftime(text_format.date_format2)
    cur_date_e = cur_date + datetime.timedelta(days = 1)
    
    return cur_date_s, cur_date_e.strftime(text_format.date_format2)

def get_cron_add_day():
    cur_date = datetime.datetime.strptime(get_kst(), text_format.date_format1)
    cur_date_s = cur_date.strftime(text_format.date_format3)
    cur_date_e = cur_date + datetime.timedelta(days = 1)
    
    return cur_date_s, cur_date_e.strftime(text_format.date_format3)

def get_7_befor_day():
    cur_date = datetime.datetime.now(timezone('Asia/Seoul')) + datetime.timedelta(weeks=-1)
    cur_date_s = cur_date.strftime(text_format.date_format3)
    cur_date_e = (cur_date + datetime.timedelta(days = 7)).strftime(text_format.date_format3)
    
    return cur_date_s, cur_date_e

def get_recently_date():
    print("get recently")
    value = local_mapper.get_recently_date()
    curDt = set_service.add_date(value, 1)
    return curDt