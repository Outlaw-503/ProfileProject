import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport
import streamlit as st
c=st.container()

with c:
  d=st.file_uploader(label="Upload Data",type="csv")
  data=pd.read_csv(d)
  a=ProfileReport(data)
  st.write(a)
