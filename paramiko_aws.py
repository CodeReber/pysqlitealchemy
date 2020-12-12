import paramiko
import os
import datetime
import secrets

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
#from setupdb import server, Base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

#DB setup
# engine = create_engine("postgresql+psycopg2://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname))
# Base.metadata.bind = engine
conn = "postgresql+psycopg2://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)
engine = create_engine(conn, echo=True)
Base = declarative_base()
DBSession = sessionmaker(bind=engine)
session = DBSession()

class server(Base):

    __tablename__ = "df_server"

    id = Column(Integer, primary_key=True)
    size_used = Column(String(255))
    date_added = Column(DateTime)

    def __init__(self, size_used, date_added):

        self.size_used = size_used
        self.date_added = date_added   




#SSH connections
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('ec2-3-14-6-104.us-east-2.compute.amazonaws.com',
            username='centos',
            key_filename='''/Users/jimpylw/aws/awsjim.pem''')
stdin, stdout, stderr = ssh.exec_command("df / | awk '{if(NR>1)print $3}'")
stdin.flush()
data = stdout.read().splitlines()
s = ""
for line in data:
    s+=(line.decode('ascii'))
print(s)
new_server = server(size_used=s, date_added=datetime.datetime.now())
session.add(new_server)
session.commit()
# conn2.execute("INSERT INTO server_size VALUES (5, 'dog','12/11/2020')")

ssh.close()