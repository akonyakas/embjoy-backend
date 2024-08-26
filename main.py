from fastapi import FastAPI
from src.api.v1.endpoints import user, journal, chat

app = FastAPI()

# app.include_router(chat.router, prefix="/chat", tags=["chat"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Pregnancy Tracker API"}


app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(journal.router, prefix="/journals", tags=["journals"])

