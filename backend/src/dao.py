from .settings import DATABASE_URI
from .shared.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DAO: 

    def __init__(self):
        self.engine = create_engine(DATABASE_URI)
        self.create_session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def connect(self):
        session = self.create_session()
        try:
            return session
        finally:
            session.close()

    def create_tables(self):
        Base.metadata.create_all(bind=self.engine)

dao: DAO = DAO()