import streamlit as st
import pandas as pd

# 공지사항 데이터프레임 불러오기
notice_df = pd.read_csv("notice.csv", encoding='utf-8')

st.title('공지사항 봇')

# 사용자가 입력한 키워드 받기
keyword = st.text_input('검색할 키워드를 입력하세요')

# 입력한 키워드로 공지사항 필터링
if keyword:
    filtered = notice_df[notice_df['제목'].str.contains(keyword)]
    if filtered.empty:
        st.write('검색 결과가 없습니다.')
    else:
        st.write(filtered)
else:
    # 최신 공지사항 정보 출력
    latest_notice = notice_df.iloc[0]
    st.write('제목:', latest_notice['제목'])
    st.write('등록일:', latest_notice['등록일'])
    st.write('링크:', latest_notice['링크'])