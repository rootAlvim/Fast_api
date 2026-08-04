from fastapi import FastAPI , Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from http import HTTPStatus
from fast_zero.schemas import Message
app = FastAPI()

templates = Jinja2Templates(directory="fast_zero/templates")

@app.get('/',status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}

@app.get('/lanpage',response_class=HTMLResponse)
def pag(req:Request):
    return templates.TemplateResponse(request=req, name="index.html")



#uvicorn app:app --reload && fastapi dev app.py