from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from calc import simple_calcultor,slicing_calcultor,draw_picture
from typing import Literal
import schemas
from exception_handlers import validation_exception_handler, zero_division_exception_handler

app = FastAPI()
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(ZeroDivisionError, zero_division_exception_handler)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("Home.html", {"request": request})

@app.post("/simpleCalculate", name="간단한 사칙연산")
async def simpleCalculate(request: schemas.SimpleCalc):
    try:
        result = simple_calcultor(request.cal_type,request.num1,request.num2)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@app.post("/slicingCalculate", name="범위 연산")
async def slicingCalculate(request: schemas.SimpleCalc):
    try:
        result = slicing_calcultor(request.cal_type,request.num1,request.num2)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/drawPicture", name="주어진 문자로 그림 그리기!")
async def drawPicture(
    select:Literal["증가","감소"], 
    word: str = Query(...,min_length=1, max_length=1), 
    count: int = Query(..., gt=0)
):
    try:
        result = draw_picture(select,word,count)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))