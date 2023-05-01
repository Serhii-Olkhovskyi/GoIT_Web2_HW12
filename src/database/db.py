from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:654321@localhost:5432/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    """
    The function opens a new database connection if there is none yet for the current application context.
    It will also create the database tables if they don't exist yet.

    :return: A database session object
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

