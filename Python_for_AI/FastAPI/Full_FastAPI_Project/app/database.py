from sqlalchemy import create_engine, sessionmaker, declarative_base


DATABASE_URL = "sqllite:///./finance.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

sessionLocal = sessionmaker(autocommit=False, autoFlush=False, bind=engine)


Base = declarative_base()
