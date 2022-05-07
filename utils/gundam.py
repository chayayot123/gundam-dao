from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.dao.gunpla_dao import GunplaDao
from utils.dao.media_dao import MediaDao

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Gundam(metaclass=Singleton):

    __gunpla_dao = None
    __media_dao = None

    def __init__(self, connection_url="sqlite:///sample.db"):
        engine = create_engine(connection_url)
        session = sessionmaker(bind=engine)
        self.__db_session = session()
        
    def get_gunpla_dao(self):
        if self.__gunpla_dao is None:
            self.__gunpla_dao = GunplaDao(session=self.__db_session)
        return self.__gunpla_dao

    def get_media_dao(self):
        if self.__media_dao is None:
            self.__media_dao = MediaDao(session=self.__db_session)
        return self.__media_dao
    
    def close(self):
        self.__db_session.close()