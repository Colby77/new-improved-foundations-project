import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv


try:
    SQLALCHEMY_DATABASE_URL = os.environ.get('DOCKER_DB_URL')
except KeyError:
    load_dotenv('.env')
    SQLALCHEMY_DATABASE_URL = os.enviorn.get('DATABASE_URL')


print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()