import datetime, requests, xmltodict, json
import corona.config as config

# Get Corona API 
def get_crn_data(corona_params):
    res = requests.get(url=config.crn_url, params=corona_params)
    data_json = xmltodict.parse(res.text)
    data = json.dumps(data_json, ensure_ascii=False, indent=4).encode('utf8')
    return json.loads(data)