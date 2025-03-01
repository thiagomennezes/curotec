from ..shared.models import Base
from sqlalchemy import Column, Integer, String

class CustomerModel(Base):
    __tablename__ = "Customer"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    person_id = Column(String, unique=True, nullable=False)
