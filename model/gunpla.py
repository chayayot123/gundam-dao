from sqlalchemy import ForeignKey,Text, Integer, Column, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class GunplaInfo(Base):
    __tablename__ = "gunpla_info"
    gunpla_id = Column(Integer, primary_key=True)
    gunpla_name = Column(Text, (30))
    media_type = Column(Text, ForeignKey("media.media_type"), nullable=False)
    rating_design = Column(Float)
    

    def __repr__(self):
        return f"GunplaInfo(gunpla_id={self.gunpla_id}, gunpla_name={self.gunpla_name}, media_type={self.media_type}, rating_design={self.rating_design})"