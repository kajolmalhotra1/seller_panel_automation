import os
import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import model
import sys
from logger.logs import Logger
from dotenv import load_dotenv

load_dotenv()

try:
    host_server = os.environ.get('DB_HOST')
    db_server_port = os.environ.get('DB_PORT')
    database_name = os.environ.get('DATABASE')
    db_email_id = os.environ.get('DB_EMAIL')
    db_password = urllib.parse.quote_plus(os.environ.get('DB_PASSWORD'))
    ssl_mode = os.environ.get('SSL_MODE')
    DATABASE_URL = "postgresql://{}:{}@{}:{}/{}?sslmode={}".format(db_email_id, db_password, host_server,
                                                                   db_server_port,
                                                                   database_name, ssl_mode)
    engine = create_engine(
        DATABASE_URL
    )

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    model.Base.metadata.create_all(bind=engine)

except Exception as e:
    exception_message = str(e)
    exception_type, exception_object, exception_traceback = sys.exc_info()
    filename = os.path.split(exception_traceback.tb_frame.f_code.co_filename)[1]
    Logger("seller_panel_GR_database").error(
        f"{exception_message} {exception_type} {filename}, Line {exception_traceback.tb_lineno}")
    raise e
