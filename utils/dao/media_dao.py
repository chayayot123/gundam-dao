from model.media_model import MediaModel
from sqlalchemy.orm.session import Session

class MediaDao:

    def __init__(self, session: Session):
        self.__session = session
    
    def get_all_media(self):
        return self.__session.query(MediaModel).all()

    def get_media_by_id(self, title_id):
        return self.__session.query(MediaModel).filter(MediaModel.title_id == title_id)[0]
    
    def get_media_by_title(self, title):
        return self.__session.query(MediaModel).filter(MediaModel.title == title).all()
    
    def get_media_by_release_date(self, release_date):
        return self.__session.query(MediaModel).filter(MediaModel.release_date == release_date).all()
    
    def add_new_timeline(self, timeline: MediaModel):
        self.__session.add(timeline)
        self.__session.commit()
        print("new timeline added to the database.")
