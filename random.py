import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


image = Image.open("canal.jpeg")
st.image(image, use_column_width=True)


st.title("CANAL+ CHRISTMAS RAFFLE DRAW APP")
st.write("Click the button below to get 30 random decoder numbers")
data_file = st.file_uploader("Upload CSV",type=["csv"])
if data_file is not None:
  if st.button('Click Me'):
    file_details = {"filename":data_file.name, "filetype":data_file.type,
                            "filesize":data_file.size}
    st.write(file_details)
    df = pd.read_csv(data_file)
    df.index = df.index + 1
    df = df.sample(n=30).reset_index().rename({'index':'Column Number'}, axis = 'columns')
    df.index = df.index + 1
    st.dataframe(df, width=1000, height=1000)
    def convert_df(df):
      return df.to_csv().encode('utf-8')
    csv = convert_df(df)
    st.download_button(
      "Download File",
      csv,
      "winners.csv",
      "text/csv",
      key='download-csv'
    )
  else:
    st.write('Thank You For Trusting Us')
else:
  st.write("You did not enter a valid file type")
