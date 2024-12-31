from sqlalchemy import Column, Integer, String, DateTime, text
from sqlalchemy.orm import declarative_base
from config import engine

Base = declarative_base()

class Gym(Base):
    __tablename__ = 'gyms_franca_wellhub'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(500), nullable=False)
    base_plan = Column(String(10), nullable=False)
    address = Column(String(500), nullable=False)
    services = Column(String(500), nullable=False)
    comorbidities = Column(String(500), nullable=False)
    date = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

Base.metadata.create_all(engine)


def create_tables():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()

