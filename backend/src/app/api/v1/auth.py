from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..core.database import get_session
from ..models.user import User, UserCreate
from ..core.security import get_password_hash, create_access_token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
router = APIRouter()

@router.post("/register")
async def register(user: UserCreate, session: Session = Depends(get_session)):
    try: 
        existing_user = session.exec(select(User).where(User.email == user.email)).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        hashed_password = get_password_hash(user.password)
        db_user = User(email=user.email, password_hash=hashed_password)
        session.add(db_user)
        session.commit()
        return {"access_token": create_access_token({"sub": db_user.email})}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_db)
):
    user = session.exec(select(User).where(User.email == form_data.username)).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {
        "access_token": create_access_token({"sub": str(user.id)}),  # Use ID instead of email
        "token_type": "bearer"
    }