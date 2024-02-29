from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
import sqlalchemy
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Boolean, func, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FlatFees(Base):
    __tablename__ = 'flat_fees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fee_name = Column(String)
    description = Column(String)
    applicable_date = Column(DateTime(timezone=True))
    value_type = Column(String)
    value = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    status = Column(Boolean)
    created_by = Column(String)
