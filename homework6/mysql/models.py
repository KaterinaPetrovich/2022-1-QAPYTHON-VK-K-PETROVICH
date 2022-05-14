from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class TotalRequestsModel(Base):
    __tablename__ = 'total_requests'

    def __repr__(self):
        return f'<total_requests: id={self.id}, count={self.count}>'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    count = Column(Integer, nullable=False)


class TypesModel(Base):
    __tablename__ = 'types'

    def __repr__(self):
        return f'<types: id={self.id}, type_name={self.type_name}, count={self.count}>'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    type_name = Column(String(500), nullable=False)
    count = Column(Integer, nullable=False)


class MostCommonModel(Base):
    __tablename__ = 'most_common'

    def __repr__(self):
        return f'<most_common: id={self.id}, url={self.url}, count={self.count}>'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    url = Column(String(500), nullable=False)
    count = Column(Integer, nullable=False)


class UserErrorModel(Base):
    __tablename__ = 'user_error'

    def __repr__(self):
        return f'<user_error: id={self.id}, url={self.url}, status={self.status}, size={self.size}, IP={self.IP}>'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    url = Column(String(500), nullable=False)
    status = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    IP = Column(String(50), nullable=False)


class ServerErrorModel(Base):
    __tablename__ = 'server_error'

    def __repr__(self):
        return f'<server_error: id={self.id}, IP={self.IP}, count={self.count}>'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    IP = Column(String(50), nullable=False)
    count = Column(Integer, nullable=False)
