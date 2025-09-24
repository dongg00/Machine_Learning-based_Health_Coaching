import streamlit as st
import pandas as pd
import time

# ----------------------------------
# 📂 데이터 로딩 함수
# ----------------------------------
file_path = "건강데이터_2022_2023.csv"  # 실제 파일명 확인 필요

@st.cache_data
def load_data():
    data = pd.read_csv(file_path)
    return data

# ----------------------------------
# 🖥️ 페이지 레이아웃 구성
# ----------------------------------
st.set_page_config(page_title="Health Data Analysis", page_icon="🍀", layout="wide")

# ----------------------------------
# 🎨 제목 및 설명
# ----------------------------------
st.title("🍀 Health Data Analysis Dashboard")
st.markdown("Summary of data visualization and clustering using Streamlit")

# ----------------------------------
# 🧭 사이드바 메뉴
# ----------------------------------
st.sidebar.header("⚙️ 설정")
show_data = st.sidebar.checkbox("데이터 미리보기")
run_process = st.sidebar.button("진행 데이터 처리 실행")

# ----------------------------------
# 📊 데이터 불러오기
# ----------------------------------
data = load_data()

if show_data:
    st.subheader("🔍 원본 데이터 미리보기")
    st.dataframe(data.head())

# ----------------------------------
# 🚀 진행 바 애니메이션
# ----------------------------------
if run_process:
    st.subheader("⏳ 데이터 처리 중...")
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        latest_iteration.text(f"처리 중... {i+1}% 완료")
        bar.progress(i + 1)
        time.sleep(0.03)

    st.success("✅ 데이터 처리 완료!")
    st.balloons()

# ----------------------------------
# 📝 기본 통계 보기
# ----------------------------------
if st.sidebar.checkbox("기본 통계 보기"):
    st.subheader("📈 기본 통계 요약")
    st.write(data.describe())
