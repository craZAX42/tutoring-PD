# pyright: reportMissingImports=false
import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.title('Tutoring Program Director Stats Analysis :smile:')
st.write('This web app is so you can analyze logged hours.')

def clean_df(df):
    columns_to_drop = ['id', 'program', 'user_id', 'program_id', 'description', 'date_of_service']
    df.drop(columns=columns_to_drop, inplace=True)
    df = df.groupby(['user'], as_index=False, sort=False)['time_recorded'].sum()
    df['time_recorded'] = df['time_recorded'].div(60)
    return df
    
uploaded_file = st.file_uploader("Put your .csv here", type='csv')
df = None
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df = clean_df(df)
st.dataframe(df)


    