from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str   

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

class User_public(BaseModel): #modelo de reposta que meu endpoint deve seguitr
    username: str
    email: EmailStr
    id: int

class UserDB(UserSchema):
    id: int