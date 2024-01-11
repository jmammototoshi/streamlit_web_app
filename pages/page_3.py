import streamlit as st
import pandas as pd

#データ分析関連
#アプリディレクトリからのパスで指定する？
df = pd.read_csv('./data/気温.csv',index_col='月')
st.dataframe(df)
st.bar_chart(df['2022'])