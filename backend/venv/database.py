from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "mysql+pymysql://root:password@localhost/blood_donation"

engine = create_engine(db_url)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)