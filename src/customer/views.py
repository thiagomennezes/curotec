from .controllers import CustomerController
from .dtos import CustomerDTO
from fastapi import APIRouter, HTTPException
from http import HTTPStatus
from typing import List, Optional

controller: CustomerController = CustomerController()
router = APIRouter(prefix="/customers", tags=["Customers"])

@router.get("/", response_model=List[CustomerDTO], description="Get Stored Customers")
def retrieve(name: Optional[str] = None, email: Optional[str] = None, person_id: Optional[str] = None, skip: int = 0, limit: int = 10):
    custom_filter = {"name": name, "email": email, "person_id": person_id}
    return controller.retrieve_all(custom_filter, skip, limit)

@router.delete("/{id}/", response_model=CustomerDTO, description="Remove Stored Customers")
def delete(id: int):
    record = controller.delete(id)
    if not record:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return record

@router.post("/", response_model=CustomerDTO, description="Store Customers")
def insert(data: CustomerDTO):
    return controller.insert(data)

@router.put("/{id}/", response_model=CustomerDTO, description="Modify Stored Customers")
def update(id: int, data: CustomerDTO):
    record = controller.update(id, data)
    if not record:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return record