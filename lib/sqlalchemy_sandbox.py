from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create the base class for our models
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())

# Persist schema to the database
if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)
    print("Database and students table created successfully.")
