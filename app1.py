
import streamlit as st
import snscrape.modules.twitter as sntwitter
import numpy as np
import pandas as pd


st.set_page_config(layout="wide")

st.header('UBM Insight')
st.subheader('Twitter Data Mining Web App')


with st.expander('About this app'):
  st.write('This web app collect the data from twitter')
  st.image('https://cdn-icons-png.flaticon.com/512/124/124021.png', width=150)
  st.write('by: UBM Insight All Team')
  st.write('by: UBM Insight All Team')
  st.write('by: UBM Insight All Team')
  st.write('by: UBM Insight All Team')



st.sidebar.header('Keyword or Hastag')
st.caption("ℹ️ Example Keyword: Indonesia")
st.caption("ℹ️ Example Hastag: #indonesia")
#st.caption("⚠️ Format dengan tanggal awal dan akhir: Indonesia until:2020-12-30 since:2020-01-01")
#st.caption("⚠️ Format dengan tanggal awal dan akhir: #indonesia until:2020-12-30 since:2020-01-01")



keyword = st.sidebar.text_input('')


st.sidebar.header('How Many Rows')
number = st.sidebar.number_input('')

st.header('Output')

col1, col2, col3= st.columns(3)

with col1:
  if keyword != '':
    st.write(f'📡 Keyword or Hastag: "{keyword}"')
  else:
    st.write('📡')


with col2:
  if number != '':
    st.write(f'🗂️ {number}')
  else:
    st.write('🗂️')



   #scraping with paramater
query = keyword   # Keyword 
limit = number

tweets = []



for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.username, tweet.content, tweet.date, tweet.url,])
        
x=pd.DataFrame(tweets, columns=['User', 'Tweet', 'Date', 'Url'])
y=x.head(3)


st.write("🪧 Shows only 3 rows:")
st.table(y)


st.write("📥 Download Full CSV File")
df = x
@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)

st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
) 
