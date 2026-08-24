from fastapi import FastAPI 
from fastapi.templating import Jinja2Templates
from fastapi import HTTPException
from http import HTTPStatus
from fast_zero.schemas import UserSchema, User_public, UserDB , UserList
app = FastAPI()

templates = Jinja2Templates(directory="templates") 

database = []

@app.get('/users/', response_model=UserList)
def users():
    return {'users': database}

@app.get('/users/{user_id}', response_model=User_public)
def search_user_id(user_id: int):
    for n in database:
        if n.id  == user_id:
            return n
        
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")  

        
@app.put('/users/{user_id}', status_code=HTTPStatus.OK, response_model=User_public)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")  
    
    new_user_id = UserDB(
        username=user.username,
        email=user.email,
        password=user.password,
        id=user_id)
    database[user_id - 1] = new_user_id 

    return new_user_id

@app.delete('/users/{user_id}', response_model=User_public)
def delete_user_id(user_id: int):
    for n in database:
        if n.id == user_id:
            database.remove(n)
            return n 
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")  



@app.post('/users/',status_code=HTTPStatus.CREATED, response_model=User_public) #POST- Criação
def create_user(user: UserSchema):
    new_user = UserDB(
        username=user.username,
        email=user.email,
        password=user.password,
        id=len(database) + 1
    )
    database.append(new_user)
    return new_user


















'''
@app.get('/',response_class=HTMLResponse)
def lan_page_test(req:Request):
    return templates.TemplateResponse(request=req, name="index.html")   ''' 
#uvicorn app:app --reload && fastapi dev app.py