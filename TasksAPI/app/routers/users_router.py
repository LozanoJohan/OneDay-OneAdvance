from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, status

from app.models.user_model import User
from app.data.data_manager import *


# Router for users
router = APIRouter()

# OAuth2PasswordRequestForm is a dependency that will be used to get the username and password from the request body
oauth2 = OAuth2PasswordBearer(tokenUrl="token")

# Algorithm to encrypt the password
crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Expiration date of the token
TOKEN_DURATION_IN_MINUTES = 1

# Secret key to encrypt the token
SECRET = "f0d031ab10f69a543acb8a1dbc589c4825bbe27e95d05c95c345654fac1deddb"




@router.get("/")
def read_root():

    return 'Welcome to my awesome TODO api 😎'




@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    
    users = get_users()
    
    user_found = next(filter(lambda user_db: user_db["id"] == user_id, users), None)

    if user_found:
        return user_found
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")




@router.get("/users/", response_model=list[User])
def read_users():

    return get_users()




@router.get("/users/name/{name}", response_model=list[User])
def read_user_by_name(name: str):

    users = get_users()
    
    users_found = filter(lambda user: user["name"] == name, users)

    return list(users_found)





@router.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    
    users = get_users()

    user_found = next(filter(lambda user_db: user_db["id"] == user.id, users), None)

    if user_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    
    user.password = crypt.hash(user.password)
    users.routerend(user.dict())

    write_data(users)

    return user




@router.delete("/users/{user_id}")
def delete_user(user_id: int):

    users = get_users()

    user_found = next(filter(lambda user_db: user_db["id"] == user_id, users), None)

    if not user_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    users.remove(user_found)

    write_data(users)

    return {"message": "User deleted"}
    



@router.put("/users/", response_model=User)
def update_user(user: User):

    users = get_users()

    user_found = next(filter(lambda user_db: user_db["id"] == user.id, users), None)

    if not user_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    user_found.update(user.dict())

    write_data(users)
    
    return user_found    
    



@router.post("/token")
async def login(form: OAuth2PasswordRequestForm =  Depends()):

    users = get_users()

    user_found = next(filter(lambda user: user["name"] == form.username 
                    and crypt.verify(form.password, user["password"]), users), None)
    
    if not user_found:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Incorrect username or password")
    
    token_duration = datetime.utcnow() + timedelta(minutes=TOKEN_DURATION_IN_MINUTES)

    access_token = {"sub": str(user_found["id"]), "exp": token_duration}
    
    return {"access_token": jwt.encode(access_token, SECRET, algorithm="HS256"), "token_type": "bearer"}




@router.get("/users/me/", response_model=User)
async def get_current_user(token: str = Depends(oauth2)):

    users = get_users()

    try:
        user_id = jwt.decode(token, SECRET, algorithms=["HS256"])["sub"]

    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Invalid token")
    
    user_found = next(filter(lambda user: str(user["id"]) == user_id, users), None)

    if not user_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="User not found")

    return user_found
  