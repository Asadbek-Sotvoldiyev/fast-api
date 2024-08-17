from fastapi import APIRouter, HTTPException, status
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from schemas import SignUpModel
from database import session, engine

auth_router = APIRouter(
    prefix='/auth'
)

session = session(bind=engine)


@auth_router.get('/')
async def signupp():
    return {'message': "This is an authentication page"}


@auth_router.post('/signup', status_code=status.HTTP_201_CREATED)
async def signup(user: SignUpModel):
    db_email = session.query(User).filter(User.email == user.email).first()
    if db_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User with this email already exists'
        )

    db_username = session.query(User).filter(User.username == user.username).first()
    if db_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User with this username already exists'
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        is_staff=user.is_staff,
        is_active=user.is_active
    )

    session.add(new_user)
    session.commit()

    data = {
        "id": new_user.id,
        'username': new_user.username,
        'email': new_user.email,
        'is_staff': new_user.is_staff,
        'is_active': new_user.is_active
    }

    response = {
        "success": True,
        'message': "User registered successfully",
        "data": data
    }

    return response
