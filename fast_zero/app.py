from fastapi import FastAPI , Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from http import HTTPStatus
from fast_zero.schemas import Message, UserSchema, User_public, UserDB
app = FastAPI()

templates = Jinja2Templates(directory="templates") 

database = []

@app.get('/',status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}

'''docs#/
@app.get('/lanpage',response_class=HTMLResponse)
def pag(req:Request):
    return templates.TemplateResponse(request=req, name="index.html")
'''

@app.post('/users/',status_code=HTTPStatus.CREATED, response_model=User_public)
def create_user(user: UserSchema):
    new_user = UserDB(
        username=user.username,
        email=user.email,
        password=user.password,
        id=len(database) + 1
    )
    database.append(new_user)
    return new_user

#uvicorn app:app --reload && fastapi dev app.py