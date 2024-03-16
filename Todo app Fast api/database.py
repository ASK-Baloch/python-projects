# database.py


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

conn_params = {
    'dbname': 'final project',
    'user': 'plugin_user',
    'password': 'abcd',
    'host': 'localhost',
    'port': '5432'
}

# Create the connection string
conn_string = "postgresql://{user}:{password}@{host}:{port}/{dbname}".format(
    **conn_params)

# Create the engine
engine = create_engine(conn_string)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
