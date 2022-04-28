from sqlalchemy import Integer, Column, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MediaModel(Base):
    __tablename__ = "medias"
    title_id = Column(Integer, primary_key=True)
    title = Column(Text, (30))
    media_type = Column(Text, (30))
    release_date = Column(Integer)
    timeline = Column(Text, (30))

    def __repr__(self):
        return f"Media(Title_id={self.title_id}, title={self.title}, media_type={self.media_type}, release_date={self.release_date}, timeline={self.timeline})"