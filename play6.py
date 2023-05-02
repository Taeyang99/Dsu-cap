import streamlit as st
import pandas as pd

# 각 카테고리별 공지사항 데이터프레임 불러오기
notice_df1 = pd.read_csv("notice1.csv", encoding='utf-8') # 카테고리 1
notice_df2 = pd.read_csv("notice2.csv", encoding='utf-8') # 카테고리 2
notice_df3 = pd.read_csv("notice3.csv", encoding='utf-8') # 카테고리 3

# 각 카테고리별 키워드로 필터링하는 함수 정의
def filter_by_keyword_category1(keyword):
    filtered = notice_df1[notice_df1['제목'].str.contains(keyword)]
    return filtered

def filter_by_keyword_category2(keyword):
    filtered = notice_df2[notice_df2['제목'].str.contains(keyword)]
    return filtered

def filter_by_keyword_category3(keyword):
    filtered = notice_df3[notice_df3['제목'].str.contains(keyword)]
    return filtered

st.등록일('공지사항 봇')

# 사용자가 선택한 카테고리 받기
category = st.selectbox('카테고리를 선택하세요', ('카테고리 1', '카테고리 2', '카테고리 3'))

# Get the keyword entered by the user
keyword = st.text_input('검색할 키워드를 입력하세요')

# 선택된 카테고리와 입력한 키워드로 공지사항 필터링
if category == '카테고리 1':
    if keyword:
        filtered = filter_by_keyword_category1(keyword)
        if filtered.empty:
            st.write('검색 결과가 없습니다')
        else:
            st.write(filtered)
    else:
        # 카테고리 1의 최신 공지사항 정보 출력
        latest_notice = notice_df1.iloc[0]
        st.write('제목:', latest_notice['제목'])
        st.write('등록일:', latest_notice['등록일'])
        st.write('링크:', latest_notice['링크'])
elif category == '카테고리 2':
    if keyword:
        filtered = filter_by_keyword_category2(keyword)
        if filtered.empty:
            st.write('검색 결과가 없습니다.')
        else:
            st.write(filtered)
    else:
        # # 카테고리 2의 최신 공지사항 정보 출력
        latest_notice = notice_df2.iloc[0]
        st.write('제목:', latest_notice['제목'])
        st.write('registration date:', latest_notice['registration date'])
        st.write('링크:', latest_notice['링크'])
else: # 카테고리 3
    if keyword:
        filtered = filter_by_keyword_category3(keyword)
        if filtered.empty:
            st.write('검색 결과가 없습니다.')
        else:
            st.write(filtered)
    else:
        # 카테고리 3의 최신 공지사항 정보 출력
        latest_notice = notice_df3.iloc[0]
        st.write('제목:', latest_notice['제목'])
        st.write('등록일:', latest_notice['등록일'])
        st.write('링크:', latest_notice['링크'])