import streamlit as st
import pandas as pd
import numpy as np
from google.cloud import storage
import os
import plotly.express as px

st.title('Reviewty KPI')

client = storage.Client.from_service_account_json('./pages/credentials/review-ty-eeab580b08fd.json')
bucket = client.get_bucket('vibey_data_kpi')
blob = bucket.blob("reviewty_kpi_merged.csv") #New one
kpi_old_path = "./pages/csv/kpi_merged.csv" #New one
blob.download_to_filename(kpi_old_path)

df = pd.read_csv(kpi_old_path)

col_select = st.multiselect(
    'Choose a column',
    (df.columns)
)

def get_chart(data= df,column_select=col_select):
    
    fig = px.line(df, x="Start Date", y=col_select)
    st.plotly_chart(fig)

get_chart(col_select)

# Object notation
with st.sidebar :
    st.text('1')
    st.text('2')