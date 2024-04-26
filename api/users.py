from typing import Optional, List
import fastapi
from pydantic import BaseModel


router = fastapi.APIRouter()

users =[]

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None

@router.get("/user", response_model=List[User])
async def get_user():
    return users

@router.post("/user")
async def create_user(user: User):
    users.append(user)
    return "Success"

@router.get("/user/{id}")
async def get_user(id: int):
    return {"user":users[id]}



# @router.get("/user/{id}")
# async def get_user(id: int = Path(..., description="The ID of the user to get", gt=2),
#                     q: str = Query(None, max_length=5),
#         ):
#     return {"user":users[id], "query":q}