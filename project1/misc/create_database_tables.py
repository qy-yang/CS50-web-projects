import os

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Date, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(r'sqlite:///E:\Backup\Yang Qianyu\cs50_web_projects\project1\books.db', echo=True)
meta = MetaData()
books = Table(
   'books', meta, 
   Column('id', Integer, primary_key = True), 
   Column('isbn', String), 
   Column('title', String), 
   Column('author', String), 
   Column('year', Date), 
)
meta.create_all(engine)
# db = scoped_session(sessionmaker(bind=engine))

print(f'Create table books')