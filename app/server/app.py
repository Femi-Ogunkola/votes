from fastapi import FastAPI

from server.routes.polls_route import router as PollsRouter
from server.routes.user_route import router as UserRouter

app = FastAPI()

app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(PollsRouter, tags=["Poll"], prefix="/poll")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}