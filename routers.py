from fastapi import APIRouter
from sqlmodel import Session,select
from schemas import UserCreate,UserRead,jwt,Userlogin
from database import engine
from models import User
from fastapi import HTTPException,Depends
from auth import get_password,verify_password,create_access_token,create_refresh_token,Oauth2_scheme,verify_access_token,verify_refresh_token
router=APIRouter()
@router.post("/registration",response_model=UserRead)
def signup(user:UserCreate):
    with Session(engine) as session:
        if(session.exec(select(User).where(User.username==user.username)).first()):
            raise HTTPException(status_code=400,detail="Username is Already exist")
        if(session.exec(select(User).where(User.email==user.email)).first()):
            raise HTTPException(status_code=400,detail="Email is Already exist")
        user_table=User(username=user.username,email=user.email,role=user.role,hash_password=get_password(user.password))
        session.add(user_table)
        session.commit()
        session.refresh(user_table)
        return user_table
@router.post("/signin",response_model=jwt)
def signin(user:Userlogin):
    with Session(engine) as session:
        user_db=session.exec(select(User).where(User.username==user.username,User.role==user.role)).first()
    if user_db:
        if(verify_password(user.password,user_db.hash_password)):
           access_token=create_access_token({"name":user.username,"role":user.role,"type":"acess token"})
           refresh_token=create_refresh_token({"name":user.username,"role":user.role,"type":"refresh token"})
           return {"access_token":access_token,
                    "refresh_token":refresh_token,
                    "token_type":"bearer"}
        else:
            raise HTTPException(status_code=401,detail="Invalid Password")
    else:
        raise HTTPException(status_code=401,detail="Invalid Username or role")
@router.get("/signin")
def get_current(token:str=Depends(Oauth2_scheme)):
    role=verify_access_token(token)
    return f"{role} is Successfully granted to you"
@router.delete("/remove/{id}")
def delete(id:int,token:str=Depends(Oauth2_scheme)):
    role=verify_access_token(token)
    if(role=="Admin"):
        with Session(engine) as session:
            user=session.get(User,id)
            if user:
                session.delete(user)
                session.commit()
                return "Successfully Deleted"
            else:
                raise HTTPException(status_code=401,detail="user not exist")
    else:
        raise HTTPException(status_code=401,detail="You not an Admin")
@router.get("/refresh")
def refresh(token:str=Depends(Oauth2_scheme)):
    payload=verify_refresh_token(token)
    if(payload["type"]=="refresh"):
        token=create_access_token({"name":payload["name"],"role":payload["role"],"type":"access token"})
        return {"new access token":token,
            "type":"bearer"}
    else:
        raise HTTPException(status_code=401,detail="Invalid Token")









 




        







