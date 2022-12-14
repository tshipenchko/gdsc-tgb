from sqlalchemy import Column, BigInteger, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)
    is_auth = Column(Boolean, default=False)
