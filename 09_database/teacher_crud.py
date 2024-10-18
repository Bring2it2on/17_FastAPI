from sqlalchemy.orm import Session
import schemas, models
from fastapi import HTTPException,status

# teacher를 저장하는 서비스 로직
def create_teacher(db : Session, teacher = schemas.TeacherCreate):

    # 저장할 teacher 객체 만들기
    db_teacher = models.Teacher(
        name=teacher.name,
        is_active=teacher.is_active,
        nickname=teacher.nickname,
        description=teacher.description
    )

    db.add(db_teacher)
    db.commit()
    
    return db_teacher

# ID로 teacher 찾기
def get_teacher_by_id(db: Session, teacher_id: int):
    found_teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()

    return found_teacher

# 모든 Teacher 찾기
def get_all_teachers(db:Session):
    # 모든 Teacher 모델 가져오가
    all_teachers = db.query(models.Teacher).all()

    return all_teachers

# teacher 수정
def update_teacher(db: Session, teacher_id:int, teacher: schemas.TeacherUpdate):

    found_teacher = get_teacher_by_id(db=db,teacher_id=teacher_id)

    if found_teacher is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not Found")
    
    if teacher.name is not None:
        found_teacher.name = teacher.name
    if teacher.is_active is not None:
        found_teacher.is_active = teacher.is_active
    if teacher.nickname is not None:
        found_teacher.nickname = teacher.nickname
    if teacher.description is not None:
        found_teacher.description = teacher.description

    db.commit()

    return found_teacher

# 삭제
def delete_teacher(db:Session, teacher_id:int):

    db.delete(get_teacher_by_id(db,teacher_id))

    db.commit()