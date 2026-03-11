from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from app.core.config import settings


#create token so that user can access the protected endpoints
def create_token(data:dict, expire_minutes=30):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(
        to_encode, 
        settings.JWT_SECRET_KEY, 
        algorithm=settings.JWT_ALGORITHM
    )

#varify the token and return the data if valid, otherwise raise an error
def verify_token(token:str):
    try:
        payload = jwt.decode(
            token, 
            settings.JWT_SECRET_KEY, 
            algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except JWTError:
        raise ValueError("Invalid token")