import streamlit as st
import pandas as pd
import os

st.set_page_config(layout='wide')
st.markdown("""
<style>
#logout-btn-container {
    position: fixed;
    bottom: 30px;
    left: 10px;
}
</style>
""", unsafe_allow_html=True)

# --- 사이드바 내부 구성 ---
with st.sidebar:

    # 고정 버튼 영역
    st.markdown('<div id="logout-btn-container">', unsafe_allow_html=True)
    if st.button("로그아웃"):
        st.session_state['Id'] = ''
        st.session_state['password'] = ''
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

#쿠키변수 login, password 초기화
if 'Id' not in st.session_state:
    st.session_state['Id'] = ''
    
if 'password' not in st.session_state:
    st.session_state['password'] = ''
    

st.title("'버츄얼 휴먼'키오스크 서비스 디자인")

if st.session_state.get('Id') != '' and st.session_state.get('password') != '':
    st.info(f"{st.session_state['Id']}님 환영합니다.")
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
            if all([name, school, age, address, grade, birthday]):
                if st.button('제출하기'):
                    st.success('제출되었습니다.')
            else:
                st.error('모두 필수 입력입니다.')
    with col2:
        if st.button('로그아웃'):
            st.session_state['Id'] = ''
            st.session_state['password'] = ''
            st.rerun()

        with st.expander('평가_Tips...'):
            st.write('Tips..')
        
        with st.expander('평가_Tips...'):
            st.write('Tips..')
else:
    cc1, cc2 = st.columns(2)
    with cc2: 
        t1, t2 = st.tabs(('로그인', '가입'))

        st.markdown("""
        <style>
        div[data-baseweb="tab-list"] button {
            margin-right: 40px;
        }
        </style>
        """, unsafe_allow_html=True)

        # 로그인 탭
        with t1: 
            Id = st.text_input('Id: ')
            password = st.text_input('Password: ')
            if st.button('로그인'):
                if all([Id, password]):
                    st.session_state['Id'] = Id
                    st.session_state['password'] = password
                    st.success('로그인이 되었습니다.')
                    st.rerun()
                else:
                    st.error('아이디와 비밀번호를 다시 입력해주세요.')

        # 가입 탭
        with t2:
            with st.form('Register'):
                school = st.text_input('학교:', key='school_input')
                grade = st.number_input('학년:', min_value=1, max_value=3, step=1)
                cls = st.number_input('반:', min_value=1, max_value=10, step=1)
                name = st.text_input('이름:', key='key_input')
                Id = st.text_input('아이디: ', key='Id_input')
                password = st.text_input('비밀번호: ', key='password_input')

                submit = st.form_submit_button('저장하기')

                if submit:
                    if all([school, grade, cls, name, Id, password]):

                        new_data = pd.DataFrame([{
                            'school': school,
                            'grade' : grade,
                            'class' : cls,
                            'name' : name,
                            'Id' : Id,
                            'password' : password
                        }])

                        FILE_NAME = "users.csv"
                        
                        if not os.path.isfile(FILE_NAME):
                            new_data.to_csv(FILE_NAME, index=False, mode='w', encoding='utf-8')
                        else:
                            new_data.to_csv(FILE_NAME, index=False, mode='a', header=False, encoding='utf-8')

                        st.success(f'{name}님의 정보가 저장되었습니다.')

                    else:
                        st.error('모두 입력해주세요.')

 
st.markdown('---')
st.write('© Park.J.H. since 2025')