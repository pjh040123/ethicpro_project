import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout='wide')

st.title('차시별로 탐구, 실습한 내용을 정리해봅시다.')

tabs = st.tabs(["1차시", "3차시", "4차시"])
#탭 간격 조절
st.markdown("""
    <style>
    div[data-baseweb="tab-list"] button {
        margin-right: 50px;
    }
    </style>
""", unsafe_allow_html=True)

with tabs[0]:
    '#### 1차시 - PhET / HeyGen'
    col1, col2 = st.columns((1,1))

    with col1:
        with st.expander("**PhET를 활용한 AI 반도체와 디스플레이의 작동 원리 시뮬레이션**"):
            components.iframe(
            src="https://phet.colorado.edu/sims/html/circuit-construction-kit-ac/latest/circuit-construction-kit-ac_all.html",
        width=800,
        height=600
    )
    with col2:
        with st.expander("**HeyGen을 활용한 버츄얼 휴먼 제작**"):
            st.write('')

with tabs[1]:
    '#### 3차시 -  Google Colab'
    col1, col2 = st.columns((2,3))

    with col1:
        with st.expander("**Google Colab 사이트**"):
            st.write("아래 버튼을 눌러 Google Colab을 실행하세요.")
            st.markdown("""
<a href="https://colab.google/">
    <button style="padding:20px 40px; font-size:18px;">Google Colab 열기</button>
</a>
""", unsafe_allow_html=True)
            st.write('')

        with st.expander("**Google Colab 실행 방법**"):
            st. write("1. 위 사이트로 접속")
            st.image("colabproject1.png")
            st.write('2. New Notebook 선택')
            st.image("colabproject2.png")
            st.write("3. 왼쪽 상단 파일 이름을 'project4'로 설정")
            st.write("왼쪽 상단 런타임 → 런타임 유형 변경 선택")
            st.image("colabproject3.png")
            st.write("하드웨어 가속기를 GPU로 설정")

    with col2:
        with st.expander('**코드 실행하기**'):
            st.markdown("""
CPU와 GPU의 처리 방식과 속도를 코딩을 통해 확인해봅시다.
                        
코드:
    
    import torch
    import time

    N = 5000

    start = time.time()
    a = torch.randn(N, N)
    b = torch.randn(N, N)
    c = torch.matmul(a, b)
    cpu_time = time.time() - start

    print(f"✅ CPU 처리시간: {cpu_time:.4f} 초")

    if torch.cuda.is_available():
        start = time.time()
        a = torch.randn(N, N, device="cuda")
        b = torch.randn(N, N, device="cuda")
        c = torch.matmul(a, b)
        torch.cuda.synchronize()
        gpu_time = time.time() - start

        print(f"⚡ GPU 처리시간: {gpu_time:.4f} 초")
    else:
        print("❌ GPU를 사용할 수 없습니다. (런타임 > GPU 설정 확인)")
                        
‼️주의점‼️
                        
    좌측 상단 런타임 → 런타임 유형 변경 → 하드웨어 가속기를 GPU로 변경해줘야 함
""")