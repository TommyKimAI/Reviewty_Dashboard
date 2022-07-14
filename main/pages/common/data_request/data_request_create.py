from socket import if_indextoname
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy import create_engine

Base = declarative_base()

class DataRequest(Base):
    __tablename__ = 'data_request'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    contents_title = Column(String, nullable=False)
    contents_detail = Column(String, nullable=False)


def main():
    engine = create_engine("sqlite:///data_request.db",echo=True)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()