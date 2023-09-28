from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Reference to DB
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'

# Connection to DB
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Models
Base = declarative_base()

# Sessions Generator
session = sessionmaker(bind=engine)


# Generator of DB connections
def get_db():
    db = session()
    try:
        yield db

    except:
        db.rollback()
        raise

    finally:
        db.close()
