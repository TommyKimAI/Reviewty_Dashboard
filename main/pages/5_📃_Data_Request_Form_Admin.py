import streamlit as st
import pandas as pd
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from pages.common import data_request_read
from sqlalchemy import create_engine
import random




engine = create_engine("sqlite:///pages/common/data_request/data_request.db")


data_request_read.select_all()
