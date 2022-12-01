from flask import Blueprint, request
from corona.model import cro_response
from corona.core import text_format, date_util
from corona.mapper import local_mapper
from corona.service import set_service
from corona.controller import app_controller
import datetime
from pytz import timezone, utc

cc = Blueprint('crn_controller', __name__)

@cc.route("/crn", methods=['POST'])
def get_crn():
    condition = set_service.get_crn_config("합계");
    data = local_mapper.get(condition)
    text = text_format.response_message_retry
    if not data:
        text = text_format.none_response_message
        return cro_response.set_data_code(200, "success", text)

    toDay = datetime.datetime.now(timezone('Asia/Seoul')).strftime(text_format.date_format4)
    incDec = data["incDec"]
    
    if int(incDec) > 0:
        text = text_format.corona_def.format(today = toDay, defCnt=data["defCnt"], incDec=incDec)
    else:
        text = text_format.corona_def_nc.format(today = toDay, defCnt=data["defCnt"])
        
    return cro_response.set_data_code(200, "success", text) 

@cc.route("/crn/oversea", methods=['POST'])
def get_oversea():
    condition = set_service.get_crn_config("합계");
    data = local_mapper.get(condition)
    text = text_format.response_message_retry
    if not data:
        text = text_format.none_response_message
        return cro_response.set_data_code(200, "success", text)

    toDay = datetime.datetime.now(timezone('Asia/Seoul')).strftime(text_format.date_format4)
    text = text_format.corona_oversea.format(today = toDay, overFlowCnt=data["overFlowCnt"])
    return cro_response.set_data_code(200, "success", text) 
    
@cc.route("/crn/local/occ", methods=['POST'])
def get_local_occ():
    content = request.get_json()
    text = text_format.response_message_retry
    if "city" not in content:
        text = text_format.none_response_message
        return cro_response.set_data_code(200, "success", text)   
    
    gubun = content['city']
    condition = set_service.get_crn_config(gubun);
    data = local_mapper.get(condition)
    toDay = datetime.datetime.now(timezone('Asia/Seoul')).strftime(text_format.date_format4)

    incDec = data["incDec"]
    
    if int(incDec) > 0:
        text = text_format.corona_local.format(today = toDay, city = data["gubun"], defCnt= data["defCnt"], incDec= data["incDec"] )
    else:
        text = text_format.corona_local_nc.format(today = toDay, city = data["gubun"], defCnt= data["defCnt"])
    
    return cro_response.set_data_code(200, "success", text)  

@cc.route("/crn/rank", methods=['POST'])
def get_rank():
    strDt = date_util.get_recently_date()
    condition = set_service.set_date_before(strDt, -1) 
    text = text_format.response_message_retry
    data = local_mapper.get_rank(condition)
    date = datetime.datetime.now().strftime("%Y년 %m월 %d일")
    if data:
        text = text_format.corona_rank.format(today = date, gubun = data[0]["gubun"], defCnt = data[0]["defCnt"])
    return cro_response.set_data_code(200, "success", text) 

@cc.route("/crn/week", methods=['POST'])
def get_week():
    curDt = date_util.get_recently_date()
    nation_list = app_controller.get_crn_local(curDt, "합계")
    text = text_format.response_message_retry
    if not nation_list:
        text = text_format.none_response_message
        return cro_response.set_data_code(200, "success", text)

    result_value = {
        "standardDt" : set_service.add_date(curDt, -1).strftime(text_format.date_format6),
        "nationList" : set_service.local_json(nation_list)["nationList"]
    }
    text = text_format.corona_week
    return  cro_response.set_data_code_list(200, "success", text , result_value)  