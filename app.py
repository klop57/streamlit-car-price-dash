import streamlit as st
from app_eda import run_eda
from app_home import run_home
from app_ml import run_ml


def _local_css():
    # 간단한 전역 스타일을 추가해서 앱을 깔끔하게 보이게 함
    st.markdown(
        """
        <style>
        /* 배경 및 폰트 */
        .stApp { font-family: 'Segoe UI', Roboto, sans-serif; }

        /* 사이드바 헤더 */
        .css-1aumxhk { padding-top: 1rem; }

        /* 카드 스타일 */
        .card { background-color: #ffffff; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); }

        /* 큰 타이틀 */
        .title { font-size:28px; font-weight:700; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main():
    _local_css()

    st.markdown("<div class='title'>자동차 구매 금액 예측 대시보드</div>", unsafe_allow_html=True)

    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)

    # 사이드바에 짧은 설명과 이미지
    st.sidebar.markdown('---')
    st.sidebar.image('./image/car.jpg', use_column_width=True)
    st.sidebar.caption('간단한 자동차 구매 예측 앱')

    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_ml()


if __name__ == '__main__':
    main()