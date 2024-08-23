from fastapi import FastAPI
from src.api.v1 import users, journals, chat

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(journals.router, prefix="/journals", tags=["journals"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pregnancy Tracker API"}
