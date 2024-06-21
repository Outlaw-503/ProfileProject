import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport
import streamlit as st
c=st.container()
with st.sidebar.header:
  d=st.sidebar.file_uploader(label="Upload Data",type="csv")
if d is not None:
  @st.cache_data
  data=pd.read_csv(d)
  a=ProfileReport(data)
  st.write(a)
