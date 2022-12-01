# from corona.service import db_service as db
from corona.service import db_service as db 
from sqlalchemy import text
from corona.core import query_format, date_util,format_util
import datetime

# Create
def insert(data:dict):
    print("local insert")
    stdDay = datetime.datetime.strptime(data["stdDay"], "%Y년 %m월 %d일 %H시")
    updateDt = date_util.get_kst()
    value:str = query_format.crn_local_value.format( 
                            deathCnt = data["deathCnt"],
                            gubunCn = data["gubunCn"],
                            gubunEn = data["gubunEn"],
                            isolClearCnt = data["isolClearCnt"],
                            isolIngCnt = data["isolIngCnt"],
                            qurRate = data["qurRate"],
                            updateDt = updateDt,
                            gubun = data["gubun"],
                            incDec = data["incDec"],
                            localOccCnt = data["localOccCnt"],
                            seq = data["seq"],
                            createDt = data["createDt"],
                            defCnt = data["defCnt"],
                            overFlowCnt = data["overFlowCnt"],
                            stdDay = stdDay)

    query = query_format.local_in.format(values = value).rstrip(",")
    db.execute(query)

def insert_list(values:dict):
    print("local insert list")
    values_query = format_util.convert_local_items(values)
    query = query_format.local_in.format(values = values_query)
    db.execute(query)

# Read
def get(condition):
    print("local get")
    value_query = query_format.local_get.format(strDt = condition["strDt"], endDt = condition["endDt"], gubun = condition["gubun"])
    value = db.execute_one(value_query)
    return value

def get_c(condition):
    print("local get")
    value_query = query_format.local_get_c.format(strDt = condition["strDt"], endDt = condition["endDt"], gubun = condition["gubun"])
    value = db.execute_one(value_query)
    return value

def get_list(condition):
    print("local get")
    value_query = query_format.local_get_list
    
    where = ""
    if "gubun" in condition:
        where = "AND `gubun` = '{gubun}'".format(gubun = condition["gubun"])
    
    value_query = value_query.format(strDt = condition["strDt"], endDt = condition["endDt"], where = where)
    value = db.execute_all(value_query)
    return value

    

def get_rank(condition):
    print("local rank")
    value_query = query_format.local_get_rank
    value_query = value_query.format(strDt = condition["strDt"], endDt = condition["endDt"])
    values = db.execute_many(value_query)
    return values

def get_data_day_cnt(seq:int)->int:
    print("get data day cnt")
    value_query = query_format.local_data_cnt.format(seq = seq)
    value = db.execute_one(value_query)
    return value[0]

def get_recently_date():
    value_query = query_format.local_get_recently_date
    value = db.execute_one(value_query)
    return value["createDt"]

# Update
def update(data:dict):
    print("local update")
    where_query = "`seq` = {seq}"
    updateDt = date_util.get_kst()
    set_query = format_util.set_local_update(data, updateDt)
    where_result = where_query.format(seq = data["seq"])
    query:str = query_format.crn_update.format(table = "local", change = set_query, where = where_result)
    db.execute(query)

# Delete 
def delete():
    print("local Delete")
    query = text(query_format.local_delete)
    db.execute(query)
