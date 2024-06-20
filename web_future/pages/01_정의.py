import streamlit as st
from PIL import Image
st.title('사물인터넷이란 무엇일까?')

st.write(
    '''
    인터넷을 통해 데이터를 다른 기기 및 시스템
    과 연결 및 교환할 목적으로 센서, 소프트웨어, 기타 기술을
    내장한 물리적 객체(사물)의 네트워크를 의미합니다.
    
    '''
    )

img = Image.open('iot.png')   
st.image(img, width=500)

st.markdown(
    '''
    ### 생산성 및 효율성 개선
    

    ### 새로운 비즈니스 모델 및 수익 흐름 창출

    
    ### 가치 창출 소요시간 단축
    
    '''
    )

st.header('🌐 사물인터넷이 중요한 이유')
st.write(
    '''
    지난 몇 년 사이에 사물인터넷은 21세기의 가장 중요한 기술 중 하나가 되었습니다.
    이제 주방 가전, 자동차, 온도 조절기, 모니터와 같은 일상 속 생활용품을 인터넷에
    연결할 수 있기 때문에 사람과 사물간의 커뮤니케이션이 가능해진 것입니다.
    
    '''
    )

st.header('🌐어떤 기술이 IoT를 가능하게 했을까')
st.markdown(
    '''
    #### 저비용, 저전력 센서 기술에 대한 접근
    - 저렴하고 안정적인 센서가 개발되면서 더 많은 제조업체가 IoT 기술을 실현할 수 있게 되었습니다.
 

    #### 연결성
    - 여러 인터넷용 네트워크 프로토콜 덕분에 센서를 클라우드 및 기타 '사물'에 손쉽게 연결할 수 있게 되면서 효율적인 데이터 전송이 가능해졌습니다.
 

    #### 클라우드 컴퓨팅 플랫폼
    - 클라우드 플랫폼의 가용성이 증가하면서 기업과 소비자 모두 확장에 필요한 인프라에 접근할 수 있게 되었습니다. 하지만 확장된 인프라를 직접 관리할 필요는 없게 되었습니다.
    
    #### 머신러닝과 분석 
    - 머신러닝 및 분석 기능이 발전하고, 클라우드에 저장된 다양하고 방대한 데이터에 대한 액세스가 가능해지자 기업들은 더욱 빠르고 편리하게 인사이트를 얻을 수 있게 되었습니다. 이와 같은 관련 기술의 출현은 계속해서 IoT의 경계를 넓히고 있으며, IoT가 생성한 데이터 역시 기술 발전에 보탬이 되고 있습니다.

    #### 대화형 인공지능(AI)
    - 신경망의 발전으로 IoT 기기에 자연어 처리(NLP) 기술이 도입되었고(디지털 개인 비서 Alexa, Cortana, Siri 등), 가정에서도 매력적이고 합리적인 가격의 IoT 기기를 활용할 수 있게 되었습니다.
    '''
    )


st.markdown(
    '''
    -[사물인터넷에 대해 더 자세히 알고 싶다면?](https://terms.naver.com/entry.naver?docId=3386810&cid=58369&categoryId=58369)
    '''
)