import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport
import streamlit as st
c=st.container()
with st.sidebar.header ("Upload data"):
  d=st.sidebar.file_uploader(label="Upload Data",type=["csv"])
if d is not None :
  @st.cache_data
  def x():
    data=pd.read_csv(d)
    return data
  u=x()
  a=ProfileReport(u,explorative=True)
  st_profile_report(a)
else:
  st.info("Upload file")
  
