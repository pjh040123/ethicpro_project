import streamlit as st
 
st.set_page_config(layout='wide')



st.title("'버츄얼 휴먼' 키오스크 디자인")
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('정보윤리에 대한 영상시청'):
        st.write('Content')
        url = 'https://youtu.be/rABDGSJm8tg?si=kD5a26KZLS7N50PO'
        st.video(url)
    with st.expander('개인정보 등록..'):
        # 학생 등록 정보를 입력해서 받는 부분
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input('이름: ', key='name')
            school = st.text_input('학교명: ', key='school')
            age = st.number_input('나이: ', min_value=1, max_value=120, step=1)
        with c2:
            address = st.text_input('주소: ', key='address')
            grade = st.selectbox('학년: ', [f'{x}학년' for x in range(1,7)], key='grade')
            birthday = st.date_input('생년월일: ', value=None, key='birthday')
        if st.button('제출하기'):
            if all([name, school, age, address, grade, birthday]):
                st.success('제출되었습니다.')
            else:
                st.error('모두 필수 입력입니다.')

with col2:
    with st.expander('평가_Tips'):
        st.write('Tips..') 

    with st.expander('평가_Tips'):
        st.write('Tips..')  
st.markdown('---')
st.write('© Park.J.H. since 2025')