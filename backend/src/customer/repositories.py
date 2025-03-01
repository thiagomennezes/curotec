from ..shared.repositories import AbstractRepository
from .models import CustomerModel

class CustomerRepository(AbstractRepository):

    model: CustomerModel = CustomerModel