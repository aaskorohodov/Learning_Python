from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///test_sql.db', echo=True)
base = declarative_base()

class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    def __rept__(self):
        return '<User(name="{}", fullname="{}")>'.format(self.name, self.fullname)

base.metadata.create_all(engine)

session = sessionmaker(bind=engine)()

user_arkady = User(name='Arkady', fullname='Arkady S')
session.add(user_arkady)
session.new
session.commit()

q = session.query(User).filter_by(name='Arkady')
other_arkady = q.first()

print(other_arkady.id)