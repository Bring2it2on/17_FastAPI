from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, HTMLResponse

# RequestValidationError 핸들러
async def validation_exception_handler(request: Request, exc: RequestValidationError):

    # 첫 번째 에러만 처리하는 예시
    first_error = exc.errors()[0] if exc.errors() else {}
    
    return JSONResponse(
        status_code=422,
        content={
            "에러내용": first_error.get("msg", "알 수 없는 오류"),
            "에러메시지": "올바른 값을 모두 입력해주세요!",
            "에러위치": first_error.get("loc", [])
        }
    )

def zero_division_exception_handler(request: Request, exc: ZeroDivisionError):
    return JSONResponse(
        status_code=400,
        content={
            "에러메시지": "0으로 나눌 수 없습니다!",
            "에러내용": str(exc)
        }
    )