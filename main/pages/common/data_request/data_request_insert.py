from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from pages.common.data_request.data_request_create import DataRequest


def insert_into(id,name,department,contents_title,contents_detail):
    engine = create_engine("sqlite:///pages/common/data_request.db",echo=True)

    with Session(engine) as session:

        r1 = DataRequest(id=id, name=name, department=department,contents_title=contents_title, contents_detail=contents_detail)

        session.add_all([r1])
        session.commit()

if __name__ == "__main__":
    insert_into()