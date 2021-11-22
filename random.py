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
  df = pd.read_excel('https://github.com/Roland-coder/canal-plus-raffle/blob/main/canal%20decoder.xlsx?raw=true',names=colnames)
  st.dataframe(df.sample(n=30))
else:
  st.write('Thank You For Trusting Us')
