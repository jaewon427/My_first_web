import streamlit as st  
import time   
import numpy as np  
import pandas as pd
from PIL import Image

st.set_page_config(  # 페이지 설정
    page_title="국내 사물인터넷 현황", # 브라우저 탭의 제목
    page_icon="📈"
    )

st.markdown("# 국내 사물인터넷 현황📈")  # st.markdown()을 이용한 헤더 작성
st.sidebar.header("현황")  # 사이드바에 헤더 작성
st.write(
    """과학기술정보통신부가 조사한 2019년도 사물인터넷 산업 실태는 다음과 같습니다."""
)

progress_bar = st.sidebar.progress(0)  # 사이드바에 진행바 생성. 현제 진행률 0%
status_text = st.sidebar.empty()  # 사이드바에 빈 텍스트 상자 생성

for i in range(1, 101):
    status_text.text("%i%% Complete" % i)
    progress_bar.progress(i)
    time.sleep(0.05)          # 0.05초 대기

chart_data = pd.DataFrame({
    '매출액': ['1,709,184', '1,881,465', '4,479,565', '2,867,732']
}) 
st.bar_chart(chart_data) 


status_text.text("%i%% Complete" % i)
time.sleep(0.05)          # 0.05초 대기

progress_bar.empty()  # 진행바 삭제

st.button("재실행")   # 버튼을 클릭하면 스크립트를 재실행함



df = pd.DataFrame({  
    '분야': ['플랫폼', '네트워크', '제품기기', '서비스'],
    '매출액': ['1,709,184', '1,881,465', '4,479,565', '2,867,732']
})

st.dataframe(df)  # DataFrame 출력

st.write(
    '''
    조사한 사업 분야는 서비스, 플랫폼, 네트워크, 디바이스 총 4개로 나누어 조사하였으며 이들 중 서비스 분야의 사업체가 1,226개사로 전체 백분율 53%를 차지하며 가장 많았습니다.
    '''
    )

img = Image.open('money.png')   
st.image(img, width=500)

st.write(
    '''
    이를 통해 과학기술정보통신부에서는 다양한 분야에 적용 가능한 사물인터넷의 혁신 기술 개발 및 확산을 통해 앞으로도 높은 성장세가 유지될 것으로 전망하고 있습니다.
    '''
    )