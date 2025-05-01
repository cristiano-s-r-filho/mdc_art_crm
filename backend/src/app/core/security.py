from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from .config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    return jwt.encode(
        {**data, "exp": expire},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
