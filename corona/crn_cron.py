from apscheduler.scheduler import Scheduler
from corona.service import cron_service
from corona.core import date_util, auth_util
from corona.core import text_format

sched = Scheduler()
sched.start()

# public Corona Data setting
def set_crn_data():
    print("Start Cron")
    reteurn_text = text_format.sys_failed
    
    if auth_util.is_auth():
        # Set Corona Data
        startDt, endDt = date_util.get_cron_add_day()
        reteurn_text = cron_service.set_crn_data_service(startDt, endDt)
    else:
        reteurn_text = text_format.auth_not_connect

sched.add_interval_job(set_crn_data, hours = 1, start_date="2020-08-21 23:38")