from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int
    username: str
    age: int


app = FastAPI()

users = []


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post('/user/{username}/{age}')
async def create_user(
        username: str = Path(min_length=5, max_length=15, description="Имя пользователя", example="MyName"),
        age: int = Path(ge=18, le=120, description="Возраст пользователя", example=20)
):
    new_id = max((user.id for user in users), default=0) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int = Path(ge=1, le=100, description="Введите id пользователя", example=1),
                      username: str = Path(min_length=5, max_length=15, description="Имя", example="UserName"),
                      age: int = Path(ge=18, le=120, description="Возраст", example=20)):
    for usr in users:
        if usr.id == user_id:
            usr.username = username
            usr.age = age
            return usr
    raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=1, le=100, description='Введите id пользователя', example=1)):
    for index, usr in enumerate(users):
        if usr.id == user_id:
            del(users[index])
            return {'id': usr.id, 'username': usr.username, 'age': usr.age}
    raise HTTPException(status_code=404, detail='User was not found')
