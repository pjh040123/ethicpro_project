import streamlit as st

st.set_page_config(layout='wide')

st.title('교과별 개념을 확인해봅시다.')

tabs = st.tabs(["정보", "미술", "사회•문화"])

#탭 간격 조절
st.markdown("""
    <style>
    div[data-baseweb="tab-list"] button {
        margin-right: 50px;
    }
    </style>
""", unsafe_allow_html=True)

#정보 교과 개념 설명
with tabs[0]:
    "#### 정보 교과에서 배운 개념들을 확인해봅시다"
    col1, col2 = st.columns((3,2))
    with col1:
        with st.expander('AI 반도체의 개념'):
            st.markdown("""
먼저 볼 개념! **반도체란?**

    정보를 계산하거나 저장하는 칩
    우리의 스마트폰, PC, AI 스피커 등 모든 전자기기 속 핵심 부품
    CPU, GPU, 메모리 등

그렇다면 **AI 반도체는?**

    AI 계산을 빠르게 하도록 특화된 칩
    AI가 하는 핵심 작업은 대량의 행렬 연산이라, CPU보다 한 번에 많은 계산을 병렬로 처리할 수 있는 구조가 필요
    그래서 등장한 것이 AI 전용 반도체
""")
        with st.expander('디스플레이의 개념'):
            st.markdown("""
**디스플레이란?**

    컴퓨터나 기기가 처리한 정보를 눈으로 볼 수 있게 보여주는 출력장치
    LCD, OLED 등
    픽셀로 구성된 화면에서 픽셀들이 빛을 내거나 조절해서 색과 이미지를 생성 
""")

    with col2:
        with st.expander('영상으로 확인하기'):
            st.write('영상을 통해 개념을 한번 더 학습해보세요.')
            url = "https://youtu.be/adtbRxg-ZOI?si=-16KXA55fvJw8Ttv&t=47"
            st.video(url)
            url = "https://youtu.be/BXnFzYg8H0k?si=8DuZDh3V9magB4bu"
            st.video(url)
        with st.expander('개념 확인하기'):
            st.write('배운 개념을 빈칸 채우기 활동을 통해 확인해봅시다.')
#미술 교과 개념 설명
with tabs[1]:
    '#### 미술 교과에서 배운 개념들을 확인해봅시다.'
    col1, col2 = st.columns((3,2))
    with col1:
        with st.expander('디자인 사고'):
            st.markdown("""
**디자인이란?**

    문제를 해결하기 위해 형태, 색, 구조 등을 계획하고 만드는 과정
    특정 목적을 달성하는 것이 중요

**디자인 사고**

    1. 공감
    사용자의 상황, 감정, 필용 등을 이해하는 단계

    2. 문제 정의
    문제를 파악하고 정리

    3. 아이디어 도출
    문제를 해결할 수 있는 다양한 아이디어 제시

    4. 시제품 제작
    아이디어를 실제로 구현해보는 단계

    5. 테스트
    사용자들에게 사용해보게 하고 문제점이나 불편사항을 다시 수정해보게 함 

""")
        with st.expander('좋은 디자인의 조건'):
            st.markdown("""
**좋은 디자인의 조건이란?**

    ①기능성
    - 목적에 맞게 제대로 작동하는가?
    - 사용자가 원하는 행동을 쉽게 할 수 있는가?

    ②심미성/조형성
    - 시각적 조화, 균형, 대비, 통일성, 리듬 등
    - 보기 좋고 직관적인가?

    ③사용성/편의성
    - 복잡하지 않고 누구나 쉽게 이해할 수 있는가?
    - 중요한 정보가 눈에 잘 띄는가?

    ④안전성
    - 사용자에게 혼란을 주지 않는가?
    - 잘못된 선택을 유도하지 않는가?

    ⑤지속 가능성
    - 환경을 해치지 않는가?
    - 재사용 가능성이나 비용 효율성이 있는가?

    ⑥독창성
    - 새로운 시도나 차별화된 아이디어가 있는가?
""")
        with st.expander('디자인의 기본 원리'):
            st.markdown("""
**디자인의 기본 원리 6가지**

    (1)대비 - 크기, 색, 형태의 차이를 활용해 중요 요소 강조

    (2)통일 - 전체적인 분위기와 느낌이 하나로 어우러지는가

    (3)균형 - 대칭, 비대칭을 활용해 안정감을 주는가

    (4)비율 - 요소들의 크기 관계가 자연스럽고 조화로운가

    (5)리듬 - 반복, 변화를 통해 시각적 흐름을 만드는가

    (6)강조 - 가장 중요한 요소가 한눈에 들어오는가
""")
    with col2:
        with st.expander('영상으로 확인하기'):
            st.write('영상을 통해 개념을 한번 더 학습해보세요.')
            url = 'https://youtu.be/hAiUT1KPgu8?si=2Ekiaf4uZ691jOg7'
            st.video(url)
            url = 'https://youtu.be/h9OWwu141Xw?si=S0HkeFFYKBDjbCnu'
            st.video(url)

#사회문화 교과 개념 설명
with tabs[2]:
    '#### 사회•문화 교과에서 배운 개념들을 확인해봅시다.'
    col1, col2 = st.columns((3,2))
    with col1:
        with st.expander('디지털 격차'):
            st.markdown("""
**디지털 격차**의 정의

    세대, 계층, 교육 수준, 경제력 등에 따라 정보통신기술을 활용할 수 있는 능력과 접근 수준에서 차이가 발생하는 현상

    예시) 고령층은 스마트 기기 경험의 부족으로 이용 시간이 오래 걸림
          장애인은 터치 스크린 조작이 어려움
          외국인, 저학력층은 언어 이해가 어려움

    디지털 기술이 확대될 수록 일부 집단의 소외 현상 강화
 """)
        with st.expander('사회적 불평등'):
            st.markdown("""
사회적 자원 접근 차원에서의 **사회적 불평등**

    정의:
    사회 구성원 간 자원, 기회, 서비스를 불평등하게 누리는 상태

    기술이 익숙한 집단은 빠르고 편리하게 이용하지만, 익숙하지 않은 사람들은 어려움을 겪음
    → 시간, 노력, 정서적 부담 등에서의 불평등 

    기술 발전은 모두에게 같은 편익을 주는 것은 아님
""")
        with st.expander('사회적 소외'):
            st.markdown("""
**사회적 소외**로의 확장

    디지털 기술은 특정 그룹을 서비스 이용 과정에서 배제시키는 기제가 될 수 있음
    
    정의:
    경제적, 사회적 활동에서 특정 개인이나 집단이 참여하지 못하고 주변화되는 현상

    예시) 키오스크 조작이 어려운 사람은 매장 이용 자체를 포기함
          장애인의 접근성은 미비하고 이용 자체가 불가능함

    → 사회 내에서 기술은 모두에게 열린 구조여야 함
""")
    with col2:
        with st.expander('영상 자료'):
            st.write('개념과 관련된 내용을 영상으로 확인하세요.')
            url = 'https://youtu.be/PTEFsDNDP5M?si=GmVrjl5Ex1BYg9g0'
            st.video(url)
            url = 'https://youtu.be/-lsnH4Kb4IQ?si=e2SN-mCvGhvKu4bg'
            st.video(url)