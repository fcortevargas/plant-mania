from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

STORAGE_URL = "postgresql://plants:pass@plants-database/plants"


def get_session():
    engine = create_engine(STORAGE_URL)

    session = scoped_session(sessionmaker(bind=engine))

    try:
        yield session
    finally:
        session.close()
