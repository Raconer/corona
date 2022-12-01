from corona.core import request_util, text_format, date_util, format_util
from corona.model.crn_local import local
from corona.mapper import local_mapper
import corona.config as config
import datetime

# public Corona Data setting
def set_crn_data_service(startDt, endDt, is_first:bool):
    corona_params = config.crn_params
    if startDt is not None and endDt is not None:
        corona_params["startCreateDt"] = startDt
        corona_params["endCreateDt"] = endDt
    
    crn_json_data = request_util.get_crn_data(corona_params)
    result_code = crn_json_data["response"]["header"]["resultCode"]
    if result_code == "00":
        crn_items = crn_json_data["response"]["body"]["items"]
        if  crn_items is not None:
            crn_data_list = crn_items["item"];
            if is_first:
                print("first")
                local_mapper.insert_list(crn_data_list);
            else:
                print("Not First")
                for crn_data in crn_data_list:
                    seq:int = crn_data["seq"]
                    crn_data_cnt:int = local_mapper.get_data_day_cnt(seq)
                    if crn_data_cnt > 0:
                        print("update")
                        local_mapper.update(crn_data)
                    else:
                        print("insert")
                        local_mapper.insert(crn_data)

        return text_format.sys_success
    else:
        return text_format.sys_failed