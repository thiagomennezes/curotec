from pydantic import BaseModel, EmailStr
from typing import Optional

class CustomerDTO(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    person_id: str

    class ConfigDict:
        from_attributes = True