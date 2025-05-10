import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import streamlit as st

def main():
    st.title("This is my streamlit app for ecomm businss that I have")
    st.sidebar.title("Upload your file")
    uploaded_file=st.sidebar.file_uploader("Upload your file , type=['csv','xlsx']")
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                pd.read_csv(uploaded_file)
            else:
                data=pd.read_excel(uploaded_file)
            st.sidebar.success("file uploaded sucessfully")
            
            st.subheader("data overview")
            st.dataframe(data.head())
            
            st.subheader("Basic information of the data")
            st.write("Shape of the data is",data.shape)
            st.write("Columns in my data",data.columns)
            st.write("missing value",data.isnull().sum())
            st.subheader("I wil show you stats of data")
            st.write(data.describe())
            
            
            
        except:
            print("it will handle if things go wrong")

if __name__=="__main__":
     main()