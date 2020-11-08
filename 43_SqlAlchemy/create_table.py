#conectando
from sqlalchemy import create_engine
engine = create_engine('sqlite:///user.db', echo=False) # :memory:

#definindo e criando a tabela
from sqlalchemy import Table, Column, Integer, String, MetaData
metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
    Column('nickname', String)
    )

metadata.create_all(engine)
