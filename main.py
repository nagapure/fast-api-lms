from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel


app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses",
    version="1.0.0",
    contact={
        "name": "Chetan", 
        "email": "chetan@gmial.com"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }
)

users =[]

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None



@app.get("/user", response_model=List[User])
async def get_user():
    return users

@app.post("/user")
async def create_user(user: User):
    users.append(user)
    return "Success"

@app.get("/user/{id}")
async def get_user(id: int = Path(..., description="The ID of the user to get", gt=2),
                    q: str = Query(None, max_length=5),
        ):
    return {"user":users[id], "query":q}