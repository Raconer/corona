from flask import Flask
from corona.controller.interceptor.interceptor import br
from corona.controller.crn_controller import cc
from corona.controller.app_controller import ac
from corona.service import main_service

import os
import corona.crn_cron

app = Flask(__name__)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="corona/corona.json"
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False

# Controller
app.register_blueprint(cc)
app.register_blueprint(ac)

# Interceptor
app.register_blueprint(br)

# Server Start Service
main_service.main_data_set();

if __name__ == "__main__":
    # app.debug = True
    app.run()