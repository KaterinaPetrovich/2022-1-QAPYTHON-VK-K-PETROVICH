from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, SmallInteger, DateTime

Base = declarative_base()


class TestUsersModel(Base):
    __tablename__ = 'test_users'

    def __repr__(self):
        return f'<test_users: id={self.id}, name={self.name}, surname={self.surname},' \
               f' middle_name={self.middle_name},username={self.username},' \
               f' password={self.password}, email={self.email}, ' \
               f'access={self.access}, active={self.active}, ' \
               f'start_active_time={self.start_active_time}'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    middle_name = Column(String(255), nullable=True)
    username = Column(String(16), nullable=True, unique=True)
    password = Column(String(255), nullable=False)
    email = Column(String(64), nullable=False, unique=True)
    access = Column(SmallInteger, nullable=True)
    active = Column(SmallInteger, nullable=True)
    start_active_time = Column(DateTime, nullable=True)