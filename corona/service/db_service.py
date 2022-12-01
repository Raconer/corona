from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
import corona.config as config
import traceback

Base = declarative_base()
engine = create_engine(config.DB_URL, encoding='utf-8', pool_recycle=3600)
Session = sessionmaker(bind=engine)



# DataBase Connectconnect_args={'': 10}
app = Flask(__name__)
engine = create_engine(config.DB_URL, encoding='utf-8', pool_recycle=3600)


db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init():
    # metadata.create_all(bind=engine)
    Base.metadata.create_all(bind=engine)

# Create
def execute(query):
    print("execute")
    value = None
    try:
        value = db_session.execute(query)
        db_session.commit()
    except SQLAlchemyError as e:
        print("Excpetion" )
        db_session.session.rollback()
        value = db_session.execute(query)
    finally:
        db_session.close()

    return value

# Read
def execute_one(query):
    print("execute_one")
    value = None
    try:
        value = db_session.execute(query).fetchone()
        db_session.commit()
    except SQLAlchemyError as e:
        print("Excpetion ONE" )
        db_session.rollback()
        value = db_session.execute(query).fetchone()
    finally:
        db_session.close()
 
    return value

def execute_all(query):
    print("execute_all")
    value = None
    try:
        value = db_session.execute(query).fetchall()
        db_session.commit()
    except SQLAlchemyError as e:
        print("Excpetion ALL" )
        db_session.rollback()
        value = db_session.execute(query).fetchall()
    finally:
        db_session.close()
    
    # try:
    #     value = db_session.execute(query).fetchall()
    # except SQLAlchemyError as e:
    #     db_session.session.rollback()
    #     value = db_session.execute(query)
    #     error = str(e.__dict__['orig'])
    #     print("Failed Execute One : ", error )
    
    # db_session.commit()
    return value

def execute_many(query):
    print("execute_many")
    value = None
    try:
        value = db_session.execute(query).fetchmany(3)
        db_session.commit()
    except SQLAlchemyError as e:
        print("Excpetion MANY" )
        db_session.rollback()
        value = db_session.execute(query).fetchmany(3)
    finally:
        db_session.close()
    
    return value

