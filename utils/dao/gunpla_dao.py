from model.gunpla_model import GunplaModel
from sqlalchemy.orm import Session

class GunplaDao:

    def __init__(self, session: Session):
        self.__session = session
    
    def get_all_gunpla(self):
        return self.__session.query(GunplaModel).all()

    def get_gunpla_by_id(self, gunpla_id):
        return self.__session.query(GunplaModel).filter(GunplaModel.gunpla_id == gunpla_id).first()
    
    def get_gunpla_by_name(self, gunpla_name):
        return self.__session.query(GunplaModel).filter(GunplaModel.gunpla_name == gunpla_name).all()
    
    def get_gunpla_by_title(self, title):
        return self.__session.query(GunplaModel).filter(GunplaModel.title == title).all()
    
    def get_gunpla_by_rating_design(self, rating_design):
        return self.__session.query(GunplaModel).filter(GunplaModel.rating_design == rating_design).all()

    def add_new_gunpla(self, gunpla_model: GunplaModel):
        self.__session.add(gunpla_model)
        self.__session.commit()
        print("new gunpla name added to the database.")
