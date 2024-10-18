from pydantic import BaseModel, Field
from typing import Literal

class SimpleCalc(BaseModel):
    cal_type: str
    num1: int
    num2: int

# class DrawPictureRequest(BaseModel):
#     select: Literal["증가", "감소"]
#     word: str = Field(...,min_length=1, max_length=1)  # 한 글자만 허용
#     count: int