# streamlit_app.py

import streamlit as st
import pymongo

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()

with st.form("Data_Request_Form"):
    name = st.text_input('Name')
    pet = st.text_input('Pet')
    input_dict = {"name":name, "pet":pet}
    submitted = st.form_submit_button()



# Pull data from the collection.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def insert_data():
    db = client.mydb
    mycol = db["mycollection"]
    mycol.insert_one(input_dict)


if submitted :
    st.write("Submit Success")
    insert_data()