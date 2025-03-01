from ..dao import dao
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

class AbstractRepository:

    model: any = None

    def __init__(self):
        self.session: Session = dao.connect()

    def delete(self, id: int) -> any:
        return self._delete(id)

    def insert(self, data: any) -> any:
        return self._insert(data)

    def retrieve_all(self, custom_filter: dict = {}, skip: int = 0, limit: int = 10) -> any:
        return self._retrieve_all(custom_filter, skip, limit)

    def update(self, id: int, data: any) -> any:
        return self._update(id, data)

    def _delete(self, id: int) -> any:
        try:
            record: any = self._retrieve_by_id(id)
            if record:
                self.session.delete(record)
                self.session.commit()
            return record
        except IntegrityError as exception:
            self.session.rollback()
            raise exception

    def _insert(self, data: any) -> any:
        try: 
            record: any = self.model(**data.model_dump(exclude={"id"}))
            self.session.add(record)
            self.session.commit()
            self.session.refresh(record)
            return record
        except IntegrityError as exception:
            self.session.rollback()
            raise exception

    def _retrieve_all(self, custom_filter: dict = {}, skip: int = 0, limit: int = 10) -> any:
        query = self.session.query(self.model)
        for key, value in custom_filter.items():
            if hasattr(self.model, key) and value is not None:
                query = query.filter(getattr(self.model, key).ilike(f"%{value}%"))
        return query.offset(skip).limit(limit).all()

    def _retrieve_by_id(self, id: int) -> any:
        return self.session.query(self.model).filter(self.model.id == id).first()

    def _update(self, id: int, data: any) -> any:
        try:
            record: any = self._retrieve_by_id(id)
            if record:
                for key, value in data.model_dump(exclude={"id"}).items():
                    setattr(record, key, value)
                self.session.commit()
                self.session.refresh(record)
            return record
        except IntegrityError as exception:
            self.session.rollback()
            raise exception
