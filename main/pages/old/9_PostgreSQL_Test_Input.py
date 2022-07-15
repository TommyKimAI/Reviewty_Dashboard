# streamlit_app.py

import streamlit as st
import psycopg2

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    st.write("Connect Success")
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.


with st.form("Data_Request_Form"):
    name = st.text_input('Name')
    pet = st.text_input('Pet')
    input_dict = {"name":name, "pet":pet}
    submitted = st.form_submit_button()

@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        conn.commit()
        st.write("Input Success")

if submitted :
    st.write("Submit Success")
    run_query(f"INSERT INTO mytable VALUES ('{name}','{pet}');")
