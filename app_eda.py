import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


@st.cache_data
def load_data(path='./data/Car_Purchasing_Data.csv'):
    return pd.read_csv(path)


def run_eda():
    # 데이터 불러오기
    df = load_data()

    st.text('이 데이터는 Car_Purchasing_Data.csv 데이터 입니다')

    radio_menu = ['데이터프레임', '기본통계', '샘플 보기']
    radio_choice = st.radio('선택하세요', radio_menu)
    if radio_choice == radio_menu[0]:
        st.dataframe(df)
    elif radio_choice == radio_menu[1]:
        st.dataframe(df.describe())
    else:
        st.dataframe(df.head())

    st.subheader('최대값 / 최소값 확인')

    # 숫자형 컬럼만 표시
    num_cols = df.select_dtypes(include=np.number).columns.tolist()
    if len(num_cols) == 0:
        st.info('숫자형 컬럼이 없습니다')
        return

    select_choice = st.selectbox('컬럼을 선택하세요', num_cols)
    st.info(f'{select_choice}는 {int(df[select_choice].min())} 부터 {int(df[select_choice].max())}까지 있습니다')

    st.subheader('상관관계 분석')

    choice_mulit_list = st.multiselect('컬럼을 2개 이상 선택하세요', num_cols, default=num_cols[:3])

    if len(choice_mulit_list) >= 2:
        corr = df[choice_mulit_list].corr(numeric_only=True)
        st.dataframe(corr)

        fig1, ax1 = plt.subplots(figsize=(6, 4))
        sb.heatmap(corr, vmin=-1, vmax=1, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.8, ax=ax1)
        st.pyplot(fig1)

    st.subheader('각 컬럼 간의 Pair Plot')
    pair_vars = ['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount']
    existing = [c for c in pair_vars if c in df.columns]
    if len(existing) >= 2:
        # seaborn pairplot은 이미지로 저장해서 출력하면 Streamlit에서 안정적으로 보임
        pair = sb.pairplot(data=df, vars=existing)
        pair.savefig('pairplot.png')
        st.image('pairplot.png', use_column_width=True)

    st.markdown('---')
    st.download_button('데이터(CSV) 다운로드', data=df.to_csv(index=False), file_name='Car_Purchasing_Data.csv', mime='text/csv')


