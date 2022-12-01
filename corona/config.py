import requests

db = {
    'user'     : '',
    'password' : '',
    'host'     : '',
    'port'     : '',
    'database' : ''
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8" 

# 공공데이터 API
crn_url = ""
crn_service_key = ""
crn_service_key_decode = requests.utils.unquote(crn_service_key)

crn_params = {
    'serviceKey' : crn_service_key_decode,
    'numOfRows' : 10,
    'pageNo' : 0
    # 'startCreateDt' : '20200821',     
    # 'endCreateDt' : '20200821'
}