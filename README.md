# Flask 외부 프로젝트

> 모든 서비스는 종료를 하였고 프로젝트 시작 하면서 Python과 flask를 공부 하면서 개발을 진행 하였습니다.
> 그래서 코드가 혼잡 합니다.
> 그래도 나중에 다시 같은 조건으로 개발을 하게 되면 조금이나마 참고를 하고자 Upload하게 되었습니다.
> 중요 정보는 지워서 프로젝트는 제대로 동작 하지는 않습니다.

APScheduler==2.1.2

Create ReadMe

# 시작 셋팅

set FLASK_APP=corona.app

# pip upgrade

python -m pip install --upgrade pip

https://velog.io/@sungjun-jin/TIL-0524-Flask-mysql-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0

# Mysql Connect

pip install sqlalchemy
pip install mysql-connector-python

# API 호출

pip install requests

# XMl을 Json으로 변경

pip install xmltodict

# Heroku 명령어

# 로그인

heroku login

# push

git push heroku master

# 기록 보기

heroku logs --tail

# Requirements update

pip freeze > requirements.txt

# 서버 정지 및 실행

# 정지

heroku ps:scale web=0

# 실행

heroku ps:scale web=1

# Scheduler

pip install apscheduler

# Clear DB Index 뒤에 숫자 1이 붙는 경우

SET @@auto_increment_increment=1;
