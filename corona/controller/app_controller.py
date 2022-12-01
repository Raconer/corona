from flask import Blueprint, request, jsonify
from corona.model import cro_response
from corona.mapper import local_mapper
from corona.service import set_service
from corona.core import text_format, date_util
from google.protobuf.json_format import MessageToJson
from corona import crn_cron
import requests
import json

import dialogflow
from google.api_core.exceptions import InvalidArgument

ac = Blueprint('app_controller', __name__)

@ac.route("/main", methods=['POST'])
def main():
    print("/main")
    curDt = date_util.get_recently_date()
    nation_list = get_crn_local(curDt, "합계")
    condition = set_service.set_date_before(curDt, -1)
    local_list = local_mapper.get_list(condition)
    crn_data = set_service.main_json(nation_list, local_list)

    return cro_response.set_data(200, "success", crn_data) 

@ac.route("/local", methods=['POST'])
def local():
    print("/local")
    content = request.json
    gubun = content['city']
    curDt = date_util.get_recently_date()
    nation_list =  get_crn_local(curDt, gubun)
    result_value = set_service.local_json(nation_list)
    return  cro_response.set_data_code(200, "success", result_value)  

@ac.route("/dialogflow", methods=['POST'])
def temp():
    print("dialogflow")
    content = request.json
    
    DIALOGFLOW_PROJECT_ID = ''
    DIALOGFLOW_LANGUAGE_CODE = 'ko'
    # GOOGLE_APPLICATION_CREDENTIALS = 'corona/corona.json'
    SESSION_ID = content['session']
    text_to_be_analyzed = content['text']
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    week_data = None
    try:
        print("try")
        response = session_client.detect_intent(session=session, query_input=query_input)
        query_result = response.query_result
        text = query_result.fulfillment_text
        context = response.query_result.output_contexts

        if context:
            data = context[0]
            if "nationList" in data.parameters.keys():

                nation_data_list = json.loads(MessageToJson(data.parameters["nationList"]))
                nation_list = []
                for nation_data in nation_data_list:
                    temp_data = {
                        'overFlowCnt' :  int(nation_data["overFlowCnt"]), # 해외 유입 증가수
                        'localOccCnt' :  int(nation_data["localOccCnt"]), # 현지 증가수
                        'incDec' : nation_data["incDec"],  # 전일 대비 증감수
                        'defCnt' :  int( nation_data["defCnt"]),  # 확진자 수
                        'createDt' :  nation_data["createDt"]
                    }
                    nation_list.append(temp_data)

                data_json = {
                    "standardDt" : data.parameters["standardDt"],
                    "nationList" : nation_list
                }
                return cro_response.set_data_code_list(200, "success", text, data_json)
    except InvalidArgument:
        print("exception")
        raise
   
    return cro_response.set_data_code(200, "success", text)

def get_crn_local(curDt, gubun:str):
    value = local_mapper.get_recently_date()
    curDt = set_service.add_date(value, 1)
    condition = set_service.set_date_before(curDt, -7)
    condition["gubun"] = gubun
    nation_list = local_mapper.get_list(condition)
    return nation_list