from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import databases
import sqlalchemy
from databases import Database

# Подключение к базе данных SQLite
DATABASE_URL = "sqlite:///./test.db"
database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Определение схемы таблицы
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("name", sqlalchemy.String, unique=True, index=True),
)

# Создание таблицы
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

# Модель для валидации данных
class UserCreate(BaseModel):
    name: str

app = FastAPI()

# Роут для создания пользователя
@app.post("/users/", response_model=UserCreate)
async def create_user(user: UserCreate):
    query = users.insert().values(name=user.name)
    user_id = await database.execute(query)
    return {"id": user_id, **user.dict()}

# Роут для получения пользователя по ID
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    user = await database.fetch_one(query)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
