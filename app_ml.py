import streamlit as st
#모델을 불러오기 위한 라이브러리
import joblib
import pandas as pd 


@st.cache_resource
def load_model(path='./model/regressor.pkl'):
    return joblib.load(path)


def run_ml():
    st.subheader('구매 금액 예측하기')

    st.info('아래 정보를 입력하면, 금액을 예측해 드립니다')

    gender_list = ['여자', '남자']
    gender = st.radio('성별을 입력하세요', gender_list, horizontal=True)

    gender_data = 0 if gender == gender_list[0] else 1

    # 입력을 컬럼으로 정리
    c1, c2, c3 = st.columns(3)
    with c1:
        age = st.number_input('나이', min_value=18, max_value=100, value=30)
    with c2:
        salary = st.number_input('연봉 (달러)', min_value=0, value=50000, step=1000, format='%d')
    with c3:
        debt = st.number_input('카드 빚 (달러)', min_value=0, value=1000, step=100)

    worth = st.number_input('자산 (달러)', min_value=0, value=10000, step=1000)

    # 작은 도움말
    st.caption('입력값은 예시이며, 실제 모델 성능은 학습 데이터와 전처리에 따라 달라집니다.')

    if st.button('예측하기!'):
        # 간단한 유효성 검사
        if salary <= 0:
            st.warning('연봉은 0보다 커야 합니다.')
            return

        try:
            regressor = load_model()
        except Exception:
            st.error('모델을 불러오지 못했습니다. model/regressor.pkl 파일을 확인하세요.')
            return

        new_data = [{'Gender': gender_data, 'Age': age, 'Annual Salary': salary, 'Credit Card Debt': debt, 'Net Worth': worth}]
        df_new = pd.DataFrame(new_data)

        try:
            y_pred = regressor.predict(df_new)
        except Exception as e:
            st.error(f'예측 중 오류가 발생했습니다: {e}')
            return

        if len(y_pred) == 0:
            st.warning('예측 결과가 없습니다')
            return

        if y_pred[0] < 0:
            st.warning('구매 금액 예측이 어렵습니다')
        else:
            price = f"${int(round(y_pred[0])):,}"
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.success(f'예측한 금액은 {price} 입니다')
            st.markdown('</div>', unsafe_allow_html=True)

