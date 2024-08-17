from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        from_attributes = True
        json_schema_extra = {
            'example': {
                'username': 'asadbek',
                'email': 'blogasadbek@gmail.com',
                'password': 'ag01120829',
                'is_staff': False,
                'is_active': True
            }
        }
