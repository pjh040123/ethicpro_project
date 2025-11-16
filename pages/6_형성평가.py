import streamlit as st
st.header('형성평가')
st.subheader('배운 내용을 차시별로 확인해봅시다.')
st.markdown('---')
for item in range(1,11):
    with st.expander(f'문제 {item}번_1번 문제입니다. 컴교에서 가장 웃긴 사람은?'):
        st.radio('보기', {'a,홍길동', 'b.홍길순', 'c.임꺽정',}, key=f'{item}번')