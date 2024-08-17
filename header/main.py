from fastapi import FastAPI, Header
from typing import Annotated
from pydantic import BaseModel, EmailStr
from fastapi.responses import RedirectResponse, Response, JSONResponse

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    fullname: str | None = None


class UserIn(UserBase):
    password: str


@app.post('/user/', response_model=UserBase)
async def user(user: UserIn):
    return user

@app.get("/sms/")
async def sms(social: str | None = None) -> Response:
    if social == "telegram":
        return RedirectResponse("https://t.me/asadbek_sotvoldiyev")
