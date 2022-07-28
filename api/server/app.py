from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from server.routes.polls_route import router as PollsRouter
from server.routes.user_route import router as UserRouter

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(PollsRouter, tags=["Poll"], prefix="/poll")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}