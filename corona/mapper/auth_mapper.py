from corona.service import db_service as db
from corona.model.crn_auth import auth
from sqlalchemy import text
from corona.core import query_format

# Create
def insert(values:auth):
    print("auth insert")
    query = text(query_format.auth_in.format(pid = values.pid,
                                                 regDate = values.regDate))
    db.execute(query);

# Read
def get() -> auth():
    query = text(query_format.auth_get)
    result = db.execute_one(query)
    return result

# Delete
def delete():
    print("auth delete")
    query = text(query_format.auth_del)
    db.execute(query)
   