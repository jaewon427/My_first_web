import streamlit as st  # streamlit 라이브러리 임포트
from PIL import Image

st.title('4차산업혁명 기술, 사물인터넷🌐')

st.subheader(
    '''
    # 무엇에 대해 배울까?
    - 사물인터넷의 정의
    - 사물인터넷의 현황
    
    '''
    )

col_1, col_2= st.columns([1,1]) # 컬럼 인스턴스 생성. 1:2:1 비율로 컬럼을 나눔

with col_1:
    img = Image.open('medical.png')   
    st.image(img, width=300)
    
with col_2:
    img = Image.open('farm.png')   
    st.image(img, width=300)

st.write('사물인터넷은 의료부터 농업에 이르기까지, 모든 산업 분야에 걸쳐 데이터와 원격 제어 기능을 제공하고 있습니다.')

st.header('🌐 사물인터넷에 대해 궁금한 것이 있나요?')
text = st.text_input('여기에 텍스트를 입력하세요') # 텍스트 입력은 입력된 값을 반환
st.write(f'입력된 텍스트: {text}')

radio = st.radio('사물인터넷에 대해 알고 있나요?', ['선택 1-알고있다', '선택 2-들어는 봤다', '선택 3-모른다']) # 라디오 버튼은 선택된 값을 반환
st.write(radio+'가 선택되었습니다.')

st.write(
    '''
    사물인터넷 기술의 핵심은 기기나 센서 등의 사물이 인터넷에 연결될 수 있도록 하는 것입니다.
    이를 위해 무선 통신 기술을 이용하여 기기들이 서로 통신하고 정보를 교환할 수 있도록 합니다.
    또한 인공지능, 빅데이터, 클라우드 등 다양한 기술을 활용하여 수집된 데이터를 분석하고 의미 있는 정보를 도출할 수 있습니다.
    '''
    )

# 레이아웃: 탭
st.header('🌐 활용방안')
tab_1, tab_2, tab_3 = st.tabs(['스마트팜', '스마트홈', '스마트 팩토리'])  # 탭 인스턴스 생성. 3개의 탭을 생성

with tab_1:
    st.write('## 스마트팜')
    st.write(
    '''
    농부들은 이제 스마트 IoT 농업 애플리케이션을 활용하여 시간과 장소에
    영향을 받지 않고 언제 어디서든 식물 수확시기를 결정하고 토양의 영양분과 수분 수준을
    감지할 수 있을 것입니다
    '''
    )
    img = Image.open('smartfarm.png')   
    st.image(img, width=600)



with tab_2:
    st.write('## 스마트홈')
    st.write(
    '''
    모바일과 같은 네트워크 기기를 이용하여 인터넷 연결만 된다면 언제 어디서든 기기와 기기를 원격
    으로 제어할 수 있을 것입니다. 사용자가 가정으로의 보안 접근, 온도, 조명, 홈씨어터 등 모든 기능을
    직접 원격으로 조절하며 지낼 수 있습니다.
    '''
    )
    img = Image.open('smarthome.png')   
    st.image(img, width=600)

with tab_3:
    st.write('## 스마트 팩토리')
    st.write(
    '''
    제조에서 디지털화의 최종 목표를 표현하는 용어입니다. 인공지능, 빅데이터 분석, 클라우드 컴퓨팅,
    산업 사물인터넷 등 4차 산업혁명의 다양한 기술들이 스마트 제조환경을 만들 것입니다.
    '''
    )
    img = Image.open('smartfactory.png')   
    st.image(img, width=600)