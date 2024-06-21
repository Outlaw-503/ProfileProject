import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport
import streamlit as st
c=st.container()
with st.sidebar.header:
  d=st.sidebar.file_uploader(label="Upload Data",type="csv")
if d is not None:
  @st.cache_data
  def x():
    data=pd.read_csv(d)
    return data
  u=x()
  a=ProfileReport(x)
  st.write(a)
else:
  st.info("Upload file")
  
