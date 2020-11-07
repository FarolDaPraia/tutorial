#usando o SQLAlchemy ORM
import sqlalchemy
# verificar versao
print(sqlalchemy.__version__)

#conectando com uma database
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

#mapeando a tabela com classes
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)

#verificando o esquema
print(User.__table__)

#criando o esquema
Base.metadata.create_all(engine)

#instanciando a classe
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
print(ed_user.name)
print(ed_user.fullname)
print(ed_user.nickname)
print(ed_user.id)

#criando uma sessao
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
session.add(ed_user)
session.commit()
our_user = session.query(User).filter_by(name='ed').first()
print(our_user)

session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])

#querying
for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)

for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)
