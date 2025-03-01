from .repositories import AbstractRepository

class AbstractController:
    repository: AbstractRepository = AbstractRepository()

    def delete(self, id: int) -> any:
        return self.repository.delete(id)

    def insert(self, data: any) -> any:
        return self.repository.insert(data)
    
    def retrieve_all(self, custom_filter: dict, skip: int, limit: int) -> any:
        return self.repository.retrieve_all(custom_filter, skip, limit)
    
    def update(self, id: int, data: any) -> any:
        return self.repository.update(id, data)