from corona.core import date_util, text_format 
from corona.service import set_service
import datetime, json

def get_crn_config_date():
    strDt, endDt = date_util.get_add_day()
    condition = {
        'strDt': strDt,
        'endDt' : endDt
    }

    return condition

def get_crn_config(gubun:str):
    strDt = date_util.get_recently_date()
    condition = set_service.set_date_before(strDt, -1)
    condition["gubun"] = gubun
    print(condition)
    return condition

def get_crn_config_7days(gubun:str):
    strDt, curDt = date_util.get_7_befor_day()
    condition = {
        'strDt': strDt,
        'curDt' : curDt,
        'gubun' : gubun
    }

    return condition

def set_date_before(curDate:datetime, days:int):
    strDt = curDate + datetime.timedelta(days=days)
    condition = {
        'strDt': strDt.strftime(text_format.date_format3),
        'endDt' : curDate.strftime(text_format.date_format3)
    }
    return condition

def set_date_after(curDate:datetime, days:int):
    endDt = curDate + datetime.timedelta(days=days)
   
    condition = {
        'strDt': curDate.strftime(text_format.date_format3),
        'endDt' : endDt.strftime(text_format.date_format3)
    }
    return condition

def add_date(curDate:datetime, days:int):
    return curDate + datetime.timedelta(days=days)

def main_json(nation_list, local_list):
    nation_data_list = []
    local_data_list = []
    nation_data = {
            'incDec' :  0, 
            'defCnt' : 0,
            'localOccCnt' : 0,    
            'overFlowCnt' : 0
        }
        
    nation_data_list = local_json(nation_list)

    nation_sum = list(filter(lambda x: x["gubun"] == "합계", local_list))[0]


    for local in local_list:
        gubun = local["gubun"]

        if gubun != "합계":
            defCnt:int = local["defCnt"]
            nation_defCnt:float = float(nation_sum["defCnt"])
            qurRate:float = ((defCnt/nation_defCnt) * 100)
            local_data = {
                'gubun' : local["gubun"],
                'overFlowCnt' : local["overFlowCnt"], 
                'localOccCnt' :  local["localOccCnt"], 
                'incDec' :  local["incDec"],
                'qurRate' : round(qurRate, 2),
                'defCnt' : defCnt
            }
            local_data_list.append(local_data)

    app_data = {
        'incDec' : nation_sum["incDec"],
        'defCnt' : nation_sum["defCnt"],
        'localOccCnt' :  nation_sum["localOccCnt"],
        'overFlowCnt' : nation_sum["overFlowCnt"],
        'standardDt' : local_list[0]["updateDt"].strftime(text_format.date_format6),
        'nations' : nation_data_list,
        'locals' : local_data_list
    }

    return app_data

def local_json(local_list):
    local_data_list = []
    for locale in local_list:
        nationDaily = {
            'overFlowCnt' :  locale["overFlowCnt"], # 해외 유입 증가수
            'localOccCnt' :  locale["localOccCnt"], # 현지 증가수
            'incDec' : locale["incDec"],  # 전일 대비 증감수
            'defCnt' : locale["defCnt"],  # 확진자 수
            'createDt' :  locale["createDt"].strftime(text_format.date_format5)
        }
        
        local_data_list.append(nationDaily)
    
    app_data = {
        'gubun': local_list[0]['gubun'],
        'nationList' : local_data_list
    }

    return app_data