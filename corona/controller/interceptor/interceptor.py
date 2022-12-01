from flask import Blueprint, request
from corona.core import text_format
from corona.model import cro_response
from corona.service.db_service import db_session
br = Blueprint('before_request', __name__)


@br.before_app_request
def before_anything():
    print("before_app_request")
    authorization = request.headers.get("Authorization")
    if authorization != "ai_company":
        print("error")
        return cro_response.set_data_code(999, text_format.error_connect, "")

