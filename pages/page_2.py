import streamlit as st

with st.form(key='profile_form'):
	name = st.text_input('名前')

	submit_btn = st.form_submit_button('送信')
	cancel_btn = st.form_submit_button('キャンセル')

	if submit_btn:
		st.text(f'ようこそ{name}さん！')