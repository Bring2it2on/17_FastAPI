from fastapi import FastAPI, Query, Path
from typing import Union

app = FastAPI()

# 각 파라미터 (사용자가 전달할 데이터)에 대해 검증과
# 추가정보 입력을 위한 기능을 제공해준다.

# query parameter validation
@app.get("/teachers")
async def print_teacher_name(

    # name은 Optional 이며 최대 20 최소 2 글자 이내로 입력
    name: Union[str,None] = Query(
        default= "bear",
        max_length=20,
        min_length=2
    )
):
    return f"teacher_name = {name}"

# 정규 표현식을 이용한 검증
@app.get("/teachers/lectures")
async def print_teacher_lecture(
    # 과목_ 로 시작하는 문자열만 허용
    lecture: str = Query(
        default="과목_Java",
        pattern="^과목_.*$"
        # ^과목_ : 문자열의 시작 ("과목_"로 시작을 해야한다는 것을 의미)
        # .* : 임의의 문자가 0개 이상 올 수 있다.
        # $ : 문자열의 끝을 의미
    )
):
    return f"lecture : {lecture}"

#  path parameter validation
@app.get("/lectures/{lecture_id}")
async def print_lecture_info(
    lecture_id: int = Path(

        # lecture_id는 0보다 크고 10보다 작아야한다.
    )
)