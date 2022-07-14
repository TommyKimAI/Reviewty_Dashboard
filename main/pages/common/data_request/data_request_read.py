from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from pages.common.data_request.data_request_create import DataRequest
from sqlalchemy import select
import streamlit as st
import pandas as pd

def select_all():
    engine = create_engine("sqlite:///pages/common/data_request.db",echo=True)
    session = Session(engine)
    
    stmt = select(DataRequest)
    for user in session.scalars(stmt):
        #st.write(user.name)
        pass
    
    df = pd.read_sql(stmt,engine)
    st.dataframe(data=df)
    print(df)

if __name__ == "__main__":
    select_all()