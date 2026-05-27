import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(page_title="스마트 계산기", page_icon="🔢", layout="centered")

st.title("🔢 내 손안의 스마트 계산기")
st.markdown("간단한 사칙연산부터 복잡한 계산까지 빠르고 정확하게 도와드립니다!")

st.divider()

# --- 입력 구역 ---
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("첫 번째 숫자를 입력하세요", value=0.0, step=1.0)
with col2:
    num2 = st.number_input("두 번째 숫자를 입력하세요", value=0.0, step=1.0)

operator = st.selectbox("원하는 연산자를 선택하세요", ["더하기 (+)", "빼기 (-)", "곱하기 (×)", "나누기 (÷)"])

st.divider()

# --- 계산 및 결과 출력 ---
st.subheader("📊 계산 결과")

if operator == "더하기 (+)":
    result = num1 + num2
    st.success(f"✨ 결과: {num1} + {num2} = **{result}**")

elif operator == "빼기 (-)":
    result = num1 - num2
    st.success(f"✨ 결과: {num1} - {num2} = **{result}**")

elif operator == "곱하기 (×)":
    result = num1 * num2
    st.success(f"✨ 결과: {num1} × {num2} = **{result}**")

elif operator == "나누기 (÷)":
    if num2 == 0:
        st.error("⚠️ 0으로 나눌 수 없습니다. 두 번째 숫자를 다시 확인해 주세요!")
    else:
        result = num1 / num2
        st.success(f"✨ 결과: {num1} ÷ {num2} = **{result:.4f}**")
