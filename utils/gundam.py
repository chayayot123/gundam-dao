from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.dao.gunpla_dao import GunplaDao
from utils.dao.media_dao import MediaDao

class Gundam:
    def __init__(self, connection_url="sqlite:///sample.db"):
        engine = create_engine(connection_url)
        session = sessionmaker(bind=engine)
        self.__db_session = session()
        
    def gunpla_info(self):
        return GunplaDao(self.__db_session)
    
    def medias(self):
        return MediaDao(self.__db_session)