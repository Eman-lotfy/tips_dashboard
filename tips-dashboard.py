import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.set_page_config(page_title='Tips dashboard', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

#loadind data
df = pd.read_csv('C:/Users/EmanLotfy/Desktop/Projects/tips/tips.csv')
#sidebar

st.sidebar.header('Tips Dashboard')
st.sidebar.image('C:/Users/EmanLotfy/Desktop/Projects/tips/tips.jpg' , use_column_width=True ,)
st.sidebar.write("")
st.sidebar.write('Filter your data:')
cat_filter =st.sidebar.selectbox('Categorical filtering' ,[None ,'sex' , 'smoker' , 'day' , 'time'])
Num_filter =st.sidebar.selectbox('Numerical filtering' ,[None ,'tip' , 'total_bill'])
Row_filter =st.sidebar.selectbox('Row filtering' ,[None ,'sex' , 'smoker' , 'day' , 'time'])
Col_filter =st.sidebar.selectbox('Column filtering' ,[None ,'sex' , 'smoker' , 'day' , 'time'])



st.sidebar.write('')
st.sidebar.markdown('Made with :heart_eyes: by Eng.[Eman Lotfy](https://www.linkedin.com/in/eman-muwafi-a8919b225/)')


#body
#row a
a1 , a2 , a3 , a4 = st.columns(4)

a1.metric('Max. total bill' , df['total_bill'].max())
a2.metric('Min. total bill' , df['total_bill'].min())
a3.metric('Max. total bill' , df['tip'].max())
a4.metric('Min. total bill' , df['tip'].min())

#row b
st.subheader("Total bill vs. tibs")
fig = px.scatter(data_frame=df , x='total_bill' , y='tip' , color=cat_filter , size=Num_filter , facet_row=Row_filter , facet_col=Col_filter)
st.plotly_chart(fig , use_container_width=True)

#row C

c1 , c2 , c3 = st.columns((4,3,3))
with c1:
    st.text('Sex vs.total bills')
    fig =px.bar(data_frame=df , x = 'sex' , y='total_bill' , color=cat_filter)
    st.plotly_chart(fig , use_container_width=True)

with c2:
    st.text('Somker/Non Smoker vs.total bills')
    fig =px.pie(data_frame=df ,names='smoker' ,values='tip' , color=cat_filter)
    st.plotly_chart(fig , use_container_width=True)

with c3:
    st.text('Day vs.tips')
    fig =px.pie(data_frame=df ,names='day' ,values='tip' , color=cat_filter , hole=0.3)
    st.plotly_chart(fig , use_container_width=True)


