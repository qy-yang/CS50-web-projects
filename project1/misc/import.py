import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# database engine object from SQLAlchemy that manages connections to the database
# DATABASE_URL is an environment variable that indicates where the database lives
engine = create_engine(r'sqlite:///E:\Backup\Yang Qianyu\cs50_web_projects\project1\books.db')
# engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# TODO: Create table 'books' if the table does not exist


f = open('./books.csv')
reader = csv.reader(f)
for isbn,title,author,year in reader:
    db.execute('INSERT INTO books (isbn,title,author,year) VALUES (:isbn, :title, :author, :year)', 
    {'isbn': isbn,'title': title, 'author': author, 'year': year})
    print(f'Added books with isbm {isbn} and title {title}')
db.commit()