from fastapi import FastAPI, Depends, HTTPException, Header
from database import Sessionlocal, engine
from models import Base, User, Donor
from auth import hash_password, verify_password, create_access_token
from sqlalchemy.orm import Session
from jose import jwt
from schemas import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str, db: Session):
    try:
        payload = jwt.decode(token, "SECRET123", algorithms=["HS256"])
        user = db.query(User).filter(User.id == payload["user_id"]).first()
        return user
    except:
        return None
    
@app.post("/signup")
def signup(user : UserCreate, db : Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(400, "user already exists")
    
    new_user = User(username = user.username, password = hash_password(user.password))
    db.add(new_user)
    db.commit()
    return {"message":"user added successfully"}

@app.post("/login")
def login(user : UserLogin,db : Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password,db_user.password):
        raise HTTPException(401, "invalid input")
    
    token = create_access_token({"user_id": db_user.id})
    return {"access_token": token}


@app.post("/donor/register")
def register_donor(
    donor: DonorCreate,
    authorization: str = Header(None),
    db: Session = Depends(get_db)
):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(401, "Missing Authorization header")

    token = authorization.split(" ")[1]
    user = get_current_user(token, db)
    if not user:
        raise HTTPException(401, "Invalid token")

    new_donor = Donor(name=donor.name,
        age=donor.age,
        gender=donor.gender,
        blood_group=donor.blood_group,
        city=donor.city,
        phone_number=donor.phone_number,
        user_id=user.id)
    db.add(new_donor)
    db.commit()
    return {"message": "Donor registered"}

@app.get("/donors")
def get_donors(
    city: str = None,
    blood_group: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Donor)
    if city:
        query = query.filter(Donor.city == city)
    if blood_group:
        query = query.filter(Donor.blood_group == blood_group)
    return query.all()