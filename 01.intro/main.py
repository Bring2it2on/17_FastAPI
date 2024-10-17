'''
FastAPI 환경설정

pip install fastapi[all]

fastapi 관련 패키지들, uvicorn

- 부분적으로 설치
pip install fastapi
pip install uvicorn
'''

# main.py : 프로젝트 전체적인 환경을 설정하는 파일

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"message" : "Hello FastAPI"}