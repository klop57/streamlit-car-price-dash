import streamlit as st
#모델을 불러오기 위한 라이브러리
import joblib
import pandas as pd 

def run_ml():
    st.subheader('구매 금액 예측하기')

    st.info('아래 정보를 입력하면, 금액을 예측해 드립니다')

    gender_list = ['여자','남자']
    gender = st.radio('성별을 입력하세요',gender_list)

    if gender == gender_list[0]:
        gender_data = 0
    else:
        gender_data = 1 

    age = st.number_input('나이를 입력하세요',min_value=20, max_value=90)

    salary = st.number_input('연봉을 입력하세요(달러)',min_value=10000)

    debt = st.number_input('카드 빛을 입력하세요(달러)',min_value=0)

    worth = st.number_input('자산을 입력하세요(달러)',min_value=10000, step = 1000)

    if st.button('예측하기!'):
        
        # 모델을 가져온다
        regressor = joblib.load('./model/regressor.pkl')

        # 유저가 입력한 데이터를 , 예측할 수 있게 가공 해야한다
        new_data = [{'Gender' : gender_data ,'Age' : age ,'Annual Salary' : salary,'Credit Card Debt' :debt , 'Net Worth' : worth}]
        df_new = pd.DataFrame(new_data)

        
        y_pred = regressor.predict(df_new)

        if y_pred < 0 :
            st.warning('구매 금액 예측이 어렵습니다')
        else:
            price = format(round(y_pred[0]), ',')

            st.info(f'예측한 금액은 {price} 달러입니다')

