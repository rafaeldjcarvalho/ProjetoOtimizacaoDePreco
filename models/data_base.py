from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class ProductDB(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    expiration_date = Column(Date)
    price = Column(Float)
    stock_quantity = Column(Integer)

DATABASE_URL = "mysql+pymysql://root:1234@localhost/dairy_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)