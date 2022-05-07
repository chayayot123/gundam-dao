from sqlalchemy import ForeignKey,Text, Integer, Column, Float
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class GunplaModel(Base):
    __tablename__ = "gunpla_info"
    gunpla_id = Column(Integer, primary_key=True)
    gunpla_name = Column(Text)
    title = Column(Text)
    rating_design = Column(Float)
    
    # medias = relationship("MediaModel", back_populates="gunpla_info")

    def __repr__(self):
        return f"GunplaModel(gunpla_id={self.gunpla_id}, gunpla_name={self.gunpla_name}, title={self.title}, rating_design={self.rating_design})"