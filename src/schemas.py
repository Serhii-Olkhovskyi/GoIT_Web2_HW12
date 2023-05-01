from datetime import date, datetime
from pydantic import BaseModel, Field, EmailStr


class ContactBase(BaseModel):
    first_name: str = Field("John", min_length=3, strict=True, max_length=50)
    last_name: str = Field("Smith", min_length=3, strict=True, max_length=50)
    email: EmailStr
    phone: int = Field("380991111111", min_length=10, strict=True, max_length=13)
    birthday: date
    user_id: int


class ContactModel(ContactBase):
    pass


class ContactUpdate(ContactModel):
    pass


class ContactResponse(ContactBase):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: int
    birthday: date
    user_id: int

    class Config:
        orm_mode = True


class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: str
    password: str = Field(min_length=6, max_length=16)


class UserDb(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    avatar: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

