from fastapi import FastAPI, Path


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: str = Path(min_length=5, max_length=15, description='Имя'),
                      age: int = Path(ge=18, le=120, description='Возраст')
                      ) -> str:
    new_id = str(int(max(users, key=int)) + 1)
    value = f"Имя: {username}, возраст: {age}"
    users[new_id] = value
    return f"User {new_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int,
                      username: str = Path(min_length=5, max_length=15, description="Имя"),
                      age: int = Path(ge=18, le=120, description='Возраст')) -> str:
    value = f"Имя: {username}, возраст: {age}"
    users[user_id] = value
    return f"The user {user_id} is updated"


@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"
