import pickle
import numpy as np
import streamlit as st
import sklearn
from xgboost import XGBRegressor

pipe = pickle.load(open("pipe.pkl",'rb'))


st.title("Laptop Price Predictor")
col1,col2,col3 = st.columns(3)

companies_list = ['Lenovo', 'Dell', 'HP', 'MSI', 'Toshiba', 'Apple', 'Asus', 'Chuwi',
       'Acer', 'Microsoft', 'Razer', 'Xiaomi', 'Samsung', 'LG',
       'Mediacom', 'Fujitsu', 'Vero', 'Huawei', 'Google']

type = ['Notebook', 'Workstation', 'Gaming', 'Ultrabook',
       '2 in 1 Convertible', 'Netbook']

cpu = ['Intel Core i5', 'Intel Core i7', 'Intel Core i3',
       'Other Intel brands', 'AMD Brands', 'Other Brands']
ram = [ 4,  8, 12, 16,  6, 24,  2, 32, 64]
os = ['Windows', 'Linux', 'Mac', 'No OS', 'Chrome', 'Android']
hdd = [1000,    0,  500, 2000,  128,   32]
ssd = [  0,  512,  256,  128,   32,   16,  768, 1000,  180,  240, 1024,
          8]
gpu = ['Nvidia', 'Intel', 'AMD', 'ARM']
with col1:
    company = st.selectbox("Select the company",companies_list)
    type_name = st.selectbox("Select the type",type)
    cpu_name = st.selectbox("Select the CPU", cpu)
    Ram = st.selectbox("Select the RAm Size", ram)
    GPU = st.selectbox("Select the GPU", gpu)
with col2:
    OS = st.selectbox("Select the OS type",os)
    weight = st.number_input("Enter the preferred weight",max_value=5.0)
    IPS = st.selectbox("Select whether IPS display or not", ['Yes', 'No'])

    X_res = st.number_input("X resolution")
    inches = st.number_input("Enter the inches ")




with col3:
    Y_res = st.number_input("Y resolution")
    touch = st.selectbox("Is touchscreen available",['Yes','No'])
    HDD = st.selectbox("Select the HDD capacity",hdd )
    SSD = st.selectbox("Select the SSD capacity", ssd)


if st.button("Predict the price"):
    if IPS =='Yes':
        IPS=1
    else:
        IPS=0

    if touch =='Yes':
        touch=1
    else:
        touch=0

    ppi= (((X_res)**2 + (Y_res)**2) **0.5)/inches

    input_vector = np.array([company,type_name,cpu_name,Ram, OS,weight,IPS,touch,ppi,HDD,SSD,GPU]).reshape(1,12)
    result =round(np.exp(pipe.predict(input_vector))[0],2)
    st.header("The predicted price of the laptop would be:")
    st.header(result)










