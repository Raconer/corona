from corona.core import text_format
import json

def get_json():
    json_data = {
        'message' : "",
        'code' : 200,
        'result' : {
            "resultMessage" : ""
        }
    }
    return json_data

def set_code(code, message):
    json_data = get_json()
    json_data["code"] = code
    json_data["message"] = message
    return json_data

def set_data(code, message, result_value):
    json_data = get_json()
    json_data["code"] = code
    json_data["message"] = message
    json_data["result"]= result_value
    return json_data

def set_data_code(code, message, text):
    json_data = get_json()
    json_data["code"] = code
    json_data["message"] = message
    json_data["result"]["resultMessage"] = text
    return json_data


def set_data_code_list(code, message, text, data):
    json_data = get_json()
    json_data["code"] = code
    json_data["message"] = message
    json_data["result"]["resultMessage"] = text
    json_data["result"]["resultData"] = data
    return json_data