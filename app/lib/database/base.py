from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

Base.to_dict = lambda: None



