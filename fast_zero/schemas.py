from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel): #Modelo de envio de dados apartir do cliente
    username: str
    email: EmailStr
    password: str

class User_public(BaseModel): #modelo de reposta que meu endpoint deve seguitr
    username: str
    email: EmailStr
    id: int

class UserDB(UserSchema):
    id: int

class UserList(BaseModel):
    users:  list[User_public]