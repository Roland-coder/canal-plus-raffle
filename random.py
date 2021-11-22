import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


st.title("CANAL+ RAFFLE DRAW APP")
st.header("CANAL+ CHRISTMAS RAFFLE DRAW APP")
st.write("Click the button below to get 30 random decoder numbers")

image = Image.open("draw.jpg")
st.image(image, use_column_width=True)

if st.button('Click Me'):
  colnames = ['Decoder Number']
  df = pd.read_csv('canalDecoder.csv',names=colnames)
  df = df.sample(n=30)
  st.dataframe(df)
else:
  st.write('Thank You For Trusting Us')
