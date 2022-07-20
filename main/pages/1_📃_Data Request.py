import streamlit as st
import psycopg2

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])
conn = init_connection()

@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        conn.commit()
        #return cur.fetchall()


st.write("This is a Request Form")
with st.form("Data_Request_Form"):
    name = st.text_input('Name')
    dep = st.text_input('Department')
    contents_title = st.text_input('Contents Title')
    contents_detail = st.text_area('Contents Detail')
    estimate_at = st.date_input('Estimate At')
    submitted = st.form_submit_button()

    if submitted :
        print('Submitted')
        st.write("Submitted")
        try : 
            run_query(f"INSERT INTO data_request(name,department,contents_title,contents_detail,estimate_at) VALUES('{name}','{dep}','{contents_title}','{contents_detail}','{estimate_at}');")
        except : 
            conn.rollback()
