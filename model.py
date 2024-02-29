import json

from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Boolean, func, ForeignKeyConstraint
from sqlalchemy import Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SlabList(Base):
    __tablename__ = 'slab_list'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cal_attribute = Column(String)
    name = Column(String)
    description = Column(DateTime(timezone=True))
    slab_start = Column(DateTime(timezone=True))
    slab_end = Column(DateTime(timezone=True))
    value_type = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    status = Column(Boolean)
    created_by = Column(String)
    tenant_id = Column(String)




