import streamlit as st
import psycopg2

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])
conn = init_connection()

@st.experimental_memo(ttl=1)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        conn.commit()
        return cur.fetchall()


st.write("This is a Request Status")

try : 
    rows = run_query("SELECT * FROM data_request;")
    for row in rows:
        st.write(row)
except:
    conn.rollback()
    rows = run_query("SELECT * FROM data_request;")
    for row in rows:
        st.write(row)

    
