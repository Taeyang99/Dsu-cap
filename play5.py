import streamlit as st
import pandas as pd

# 공지사항 데이터프레임 불러오기
notice_df = pd.read_csv("notice.csv", encoding='utf-8')

st.title('공지사항 봇')

# 사용자가 선택한 카테고리 받기
category = st.selectbox('카테고리를 선택하세요', ['전체', '학사', '장학', '입학'])

# 사용자가 입력한 키워드 받기
keyword = st.text_input('검색할 키워드를 입력하세요')

# 입력한 키워드와 카테고리로 공지사항 필터링
if category == '전체':
    filtered = notice_df[notice_df['제목'].str.contains(keyword)]
else:
    filtered = notice_df[(notice_df['제목'].str.contains(keyword)) & (notice_df['카테고리'] == category)]

if filtered.empty:
    st.write('검색 결과가 없습니다.')
else:
    st.write(filtered)