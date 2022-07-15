import streamlit as st
import pandas as pd
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
import os
print(os.getcwd())
from pages.common.data_request import data_request_insert
from sqlalchemy import create_engine
import random




engine = create_engine("sqlite:///pages/common/data_request/data_request.db")

with st.form("Data_Request_Form"):
    #Columns
    st.write("Inside the form")
    name = st.text_input('Name')
    dep = st.text_input('Department')
    contents_title = st.text_input('Contents Title')
    contents_detail = st.text_area('Contents Detail')
    #requested_at = st.date_input('Requested At')
    #estimate_at = st.date_input('Estimate At')
    
    #Submit
    submitted = st.form_submit_button()
    if submitted :
        st.write("Submit Success")
        id= random.randrange(1,10000)
        data_request_insert.insert_into(id,name,dep,contents_title,contents_detail)
