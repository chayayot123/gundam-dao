from sqlalchemy import Integer, Column, Text
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MediaModel(Base):
    __tablename__ = "medias"
    title_id = Column(Integer, primary_key=True)
    title = Column(Text)
    media_type = Column(Text)
    release_date = Column(Integer)
    timeline = Column(Text)

    # gunpla_info = relationship("GunplaModel", back_populates="medias")

    def __repr__(self):
        return f"Media(Title_id={self.title_id}, title={self.title}, media_type={self.media_type}, release_date={self.release_date}, timeline={self.timeline})"