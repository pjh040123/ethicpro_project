import streamlit as st

st.set_page_config(layout='wide')

st.header("📄 활동 내용 기록하기")
st.subheader('차시별 활동 내용을 포트폴리오 형식으로 자유롭게 기록해봅시다.')

content = st.text_area("문서 내용을 작성하세요:", height=400)

if st.button("저장"):
    with open("note.txt", "w", encoding="utf-8") as f:
        f.write(content)
    st.success("✅ 문서가 저장되었습니다!")

# 저장된 파일 불러오기
if st.button("불러오기"):
    try:
        with open("note.txt", "r", encoding="utf-8") as f:
            loaded = f.read()
        st.text_area("불러온 문서", loaded, height=400)
    except FileNotFoundError:
        st.warning("저장된 문서가 없습니다.")