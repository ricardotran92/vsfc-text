import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np

class_list = {'0': 'Negative', '1': 'Positive', '2': 'Positive'}

st.title('Sentiment analysis from Vietnamese students\' feedback')

image = Image.open('feedback.jpg')
st.image(image)

input_ec = open('ec_vsfc_pkl', 'rb')
model 


