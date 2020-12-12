from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import secrets

# conn = "postgresql+psycopg2://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)
# engine = create_engine(conn, echo=True)
# Base = declarative_base()
conn = "sqlite:///new.db"
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


Base.metadata.create_all(engine)

new_server = server(size_used='test', date_added=datetime.datetime.now())
session.add(new_server)
session.commit()