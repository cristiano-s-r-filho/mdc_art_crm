from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select
from jose import JWTError, jwt
from app.core.database import get_session
from app.core.security import settings  # Renamed from .core.security import settings
from app.models.user import User
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_db_session():
    return Depends(get_session)

async def require_auth(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="auth/login")),
    session: Session = Depends(get_session)
):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user = session.get(User, payload.get("sub"))
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")