from typing import Dict
from fastapi import FastAPI, HTTPException, status, Depends
from models.user import User
import json
from routers.tasks import router as tasks_router
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

app = FastAPI()
app.include_router(tasks_router)

oauth2 = OAuth2PasswordBearer(tokenUrl="token")

crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

TOKEN_DURATION_IN_MINUTES = 1
SECRET = "f0d031ab10f69a543acb8a1dbc589c4825bbe27e95d05c95c345654fac1deddb"

with open("./data/users_fake_db.json", "r+") as file:
    users: list[Dict] = json.load(file)



@app.get("/")
def read_root():
    return 'Welcome to my awesome TODO api 😎'




@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):

    user_found = next(filter(lambda user_db: user_db["id"] == user_id, users), None)

    if user_found:
        return user_found
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")




@app.get("/users/", response_model=list[User])
def read_users():

    return users




@app.get("/users/name/{name}", response_model=list[User])
def read_user_by_name(name: str):

    users_found = filter(lambda user: user["name"] == name, users)

    return list(users_found)




@app.patch("/users/{user_id}", status_code=status.HTTP_202_ACCEPTED)
def set_user_done(user_id: int):

    user_found = next(filter(lambda user_db: user_db["id"] == user_id, users), None)

    try:
        user_found.update({"completion_status": True})

        with open("./data/users_fake_db.json", "w") as file:
            json.dump(users, file, indent=4)

        return user_found

    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")




@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    
    user_found = next(filter(lambda user_db: user_db["id"] == user.id, users), None)

    if user_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user already exists")
    
    user.password = crypt.hash(user.password)
    users.append(user.dict())

    with open("./data/users_fake_db.json", "w") as file:
        json.dump(users, file, indent=4)

    return user




@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    user_found = next(filter(lambda user_db: user_db["id"] == user_id, users), None)

    if user_found:

        users.remove(user_found)

        with open("./data/users_fake_db.json", "w") as file:
            json.dump(users, file, indent=4)

        return user_found
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")




@app.put("/users/", response_model=User)
def update_user(user: User):

    user_found = next(filter(lambda user_db: user_db["id"] == user.id, users), None)

    if user_found:

        user_found.update(user.dict())
    
        with open("./data/users_fake_db.json", "w") as file:
            json.dump(users, file, indent=4)
        
        return user_found
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")




@app.post("/token")
async def login(form: OAuth2PasswordRequestForm =  Depends()):

    user_found = next(filter(lambda user: user["name"] == form.username 
                    and crypt.verify(form.password, user["password"]), users), None)
    
    if not user_found:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Incorrect username or password")
    
    token_duration = datetime.utcnow() + timedelta(minutes=TOKEN_DURATION_IN_MINUTES)

    access_token = {"sub": str(user_found["id"]), "exp": token_duration}
    
    return {"access_token": jwt.encode(access_token, SECRET, algorithm="HS256"), "token_type": "bearer"}




@app.get("/users/me/", response_model=User)
async def get_current_user(token: str = Depends(oauth2)):

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
  


# TODO: Auth users
# TODO: Query by user
# TODO: MongoDB
# TODO: Error handling
    

