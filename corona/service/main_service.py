from corona.model.crn_local import local
from corona.mapper import auth_mapper, local_mapper
from corona.service import cron_service
from corona.core import date_util, auth_util
import datetime

def main_data_set():
    auth_mapper.delete()

    if auth_util.is_auth():
        local_mapper.delete()
        startDt, endDt = date_util.get_7_befor_day()
        cron_service.set_crn_data_service(startDt, endDt, True) 