from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://inventory_knse_user:W6PKDpgHHJ9VUzHmkMqJuUEnc0mkqfge@dpg-crmf2iq3esus73fs09r0-a.oregon-postgres.render.com/inventory_knse" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
