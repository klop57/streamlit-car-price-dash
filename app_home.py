import streamlit as st
import pandas as pd


def run_home():
    st.subheader('자동차 데이터를 분석하고, 예측하는 앱')

    # 히어로 섹션
    col1, col2 = st.columns([2, 3])
    with col1:
        st.image('./image/car.jpg', use_container_width=True)
    with col2:
        st.markdown("""
        ### 깔끔하고 직관적인 인터페이스
        이 앱은 자동차 구매 관련 데이터를 시각화하고, 사용자의 입력을 바탕으로
        구매 금액을 예측합니다. 아래의 EDA 탭에서 데이터를 확인하고, ML 탭에서
        직접 예측을 시도해 보세요.
        """)

    # 간단한 데이터 요약 메트릭
    try:
        df = pd.read_csv('./data/Car_Purchasing_Data.csv')
        c1, c2, c3 = st.columns(3)
        c1.metric('행 수', df.shape[0])
        c2.metric('열 수', df.shape[1])
        c3.metric('평균 구매액', f"${int(df['Car Purchase Amount'].mean()):,}")
    except Exception:
        st.info('데이터를 불러오지 못했습니다. EDA에서 데이터 파일을 확인하세요.')

    st.markdown('---')
    st.markdown('프로젝트 설명')
    st.write('데이터는 캐글의 Car_Purchasing_Data.csv를 사용했습니다. 이 샘플 앱은 Streamlit으로 제작되었으며, 간단한 ML 예측과 EDA를 포함합니다.')
    