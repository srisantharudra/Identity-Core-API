from pwdlib import PasswordHash
from fastapi import HTTPException
from datetime import datetime,timedelta
from jose import jwt,JWTError
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
import os
import secrets
load_dotenv()
secret_key=os.getenv("Secret_Key")
password_hash=PasswordHash.recommended()
def get_password(password:str):
    return password_hash.hash(password)
def verify_password(password1:str,password2:str):
    return password_hash.verify(password1,password2)
def create_access_token(data:dict):
    to_encode=data.copy()
    expiry=datetime.utcnow()+timedelta(minutes=30)
    to_encode["exp"]=expiry
    jwt_token=jwt.encode(to_encode,secret_key,algorithm="HS256")
    return jwt_token
Oauth2_scheme=OAuth2PasswordBearer(tokenUrl="signin")
def create_refresh_token(data:dict):
    to_encode=data.copy()
    exp=datetime.utcnow()+timedelta(days=7)
    to_encode["exp"]=exp
    token=jwt.encode(to_encode,
               secret_key,
               algorithm="HS256")
    return token
def verify_access_token(token:str):
    try:
        payload=jwt.decode(token,
                        secret_key,
                        algorithms=["HS256"])
        return payload["role"]
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid Token")
def verify_refresh_token(token:str):
    try:
        payload=jwt.decode(token,
               secret_key,
               algorithms="HS256")
        return payload
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid Token")
    
    
    
        
    
    
    




    