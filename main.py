import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np

class_list = {'0': 'Negative', '1': 'Positive', '2': 'Positive'}

st.title('Sentiment analysis from Vietnamese students\' feedback')

image = Image.open('feedback.jpg')
st.image(image)

input_ec = open('ec_vsfc.pkl', 'rb')
encoder = pkl.load(input_ec)

input_md = open('lrc_vsfc.pkl, 'rb')
model = pkl.load(input_md)

st.header('Write a feedback')
txt = st.text_area('', '')


