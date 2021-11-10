from typing import List
from uuid import UUID

import uvicorn
from fastapi import FastAPI

from inmemory_models import User, Gender, Role

app: FastAPI = FastAPI()

users: List[User] = [
    User(id=UUID('20455ac9-00d4-4645-84d6-922190c31227'), first_name="Jamila", last_name="Ahmed", gender=Gender.female,
         roles=[Role.student]),
    User(id=UUID('216288db-7bb5-47d6-a52a-37e5d2baba77'), first_name="Alex", last_name="Jones", gender=Gender.male,
         roles=[Role.admin, Role.user])
]


@app.get("/")
async def greeting() -> dict[str]:
    return dict(Say='greeting')


@app.get("/api/v1/users")
async def find_users() -> List[User]:
    return users;


@app.post("/api/v1/users")
async def register_user(user: User) -> dict[str, UUID]:
    users.append(user)
    return dict(id=user.id)


if __name__ == '__main__':
    uvicorn.run(app=app, port=8080, host="0.0.0.0")
