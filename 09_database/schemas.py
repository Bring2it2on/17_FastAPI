from pydantic import BaseModel
from typing_extensions import Optional
# request 받거나, response를 받을때
class TeacherBase(BaseModel):
    name: str
    is_active: bool
    nickname: Optional[str] = None
    description: Optional[str] = None

# 업데이트할 때 사용되는 request모델
class TeacherUpdate(BaseModel):
    name: Optional[str] = None
    is_active: Optional[bool] = None
    nickname: Optional[str] = None
    description: Optional[str] = None

# SqlAlchemy 모델 : 데이터베이스의 통신을 위한 데이터 구조정의
# Pydantic 모델:

# request 요청 모델
class TeacherCreate(TeacherBase):
    pass

# response 응답 모델
class TeacherResponse(TeacherBase):
    id: int


# 학생
class StudentBase(BaseModel):
    name: str
    lunch_menu: Optional[str] = None
    nickname: Optional[str] = None
    description: Optional[str] = None

# 업데이트할 때 사용되는 request모델
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    lunch_menu: Optional[str] = None
    nickname: Optional[str] = None
    description: Optional[str] = None

# request 요청 모델
class StudentCreate(StudentBase):
    pass

# response 응답 모델
class StudentResponse(StudentBase):
    id: int