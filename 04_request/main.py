from fastapi import FastAPI, Request
from typing import Optional

app = FastAPI()

@app.get("/items/")
async def read_items(request : Request):
    # 클라이언트 ip
    host = request.client.host
    # Request 객체로 확인 가능한 것
    # body() : 본문
    # headers : 헤더
    return {"clienthost:" : host}

# request Body
# 클래스타입으로 만들고, BaseModel을 상속받아 구현한다.
from pydantic import BaseModel

class Teacher(BaseModel):
    is_working: bool
    name: str
    nickname: Optional[str] = None

@app.post("/teachers")
async def teacher_info(teacher: Teacher):

    if teacher.nickname:
        return f"안녕하세요 제 닉네임은 {teacher.nickname}이고, 현재 일하는 상태는 {teacher.is_working} 입니다."
    return f"안녕하세요 제 이름은 {teacher.name}이고, 현재 일하는 상태는 {teacher.is_working} 입니다."

# path_parameter
# query_parameter
# requestBody

# 만들어보기

# student_no : path_parameter로 받고 int
# Student : requestBody (이름(str), 나이(int))
# lecture_name : query_parameter

# student no, name, age, lecture_name을 전부 출력하는
# 문자열로 return 해주는 api

class Student(BaseModel):
    name: str
    age: int

@app.post("/students/{student_no}")
async def student_info(student: Student, lecture_name : str, student_no : int):

    return (f"student_no: {student_no} name: {student.name} age: {student.age} lecture_name: {lecture_name}")

