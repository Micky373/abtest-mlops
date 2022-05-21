import streamlit as st
import pandas as pd

def app():
    st.title('In this page we display all the datasets')
    
    st.title('**This is the `Chrome browser users` dataset**')
    df = pd.read_csv('./data/chrome_data.csv')
    st.write(df)

    st.title('**This is the `Chrome mobile view browser users` dataset**')
    df = pd.read_csv('./data/chrome_mobile_webView_data.csv')
    st.write(df)

    st.title('**This is the `Facebook users` dataset**')
    df = pd.read_csv('./data/facebook_data.csv')
    st.write(df)

    st.title('**This is the `Platform 6 users` dataset**')
    df = pd.read_csv('./data/platform_5.csv')
    st.write(df)

    st.title('**This is the `Platform 5 users` dataset**')
    df = pd.read_csv('./data/platform_6.csv')
    st.write(df)
