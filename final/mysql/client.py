import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
from mysql.models import Base, TestUsersModel


class MysqlClient:

    def __init__(self, user, port, password, host, db_name):
        self.user = user
        self.port = port
        self.password = password
        self.host = host
        self.db_name = db_name

        self.connection = None
        self.engine = None
        self.session = None

    def connect(self, db_created=True):

        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'
        self.engine = sqlalchemy.create_engine(url)
        self.connection = self.engine.connect()

        session = sessionmaker(bind=self.connection.engine)
        self.session = session()

    def create_db(self):
        self.connect(db_created=False)
        self.execute_query(f'DROP database IF EXISTS {self.db_name}')
        self.execute_query(f'CREATE database {self.db_name}')

    def delete_db(self):
        self.execute_query(f'DROP database IF EXISTS {self.db_name}')

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def truncate_test_users(self):
        self.execute_query(f'TRUNCATE test_users')


    def execute_query(self, query, fetch=False):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def check_by_username(self, username):
        return self.session.query(TestUsersModel).filter(TestUsersModel.username==username).first()
