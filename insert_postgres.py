import os
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import secrets

#DB setup
conn = "postgresql+psycopg2://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)
engine = create_engine(conn)
conn2 = engine.connect()
conn2.execute("INSERT INTO server_size VALUES (4, '2344','12/12/2020')")
# with engine.connect() as connection:
#     result = connection.execute("select * from climate_compile")
#     for row in result:
#         print(row)
# Base.metadata.bind = engine
