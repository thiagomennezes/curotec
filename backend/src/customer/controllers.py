from ..shared.controllers import AbstractController
from .repositories import CustomerRepository


class CustomerController(AbstractController):
    repository: CustomerRepository = CustomerRepository()