import streamlit as st
import random

# --- 페이지 설정 ---
st.set_page_config(page_title="스마트 계산기", page_icon="🔢", layout="centered")

# --- 🤫 탑 시크릿 이스터에그 기능 (이름 궁합) ---
# 사이드바나 보이지 않는 곳에 숨겨두어 아는 사람만 쓸 수 있는 재미 요소입니다!
with st.sidebar.expander("🤫 비밀의 방 (이스터에그)"):
    st.write("💘 이름으로 보는 운명의 궁합!")
    name1 = st.text_input("나의 이름", key="egg_name1")
    name2 = st.text_input("상대의 이름", key="egg_name2")
    if name1 and name2:
        # 이름 길이를 이용해 고정된 재미용 점수 생성 (항상 같은 결과가 나오도록 시드 고정)
        random.seed(len(name1) + len(name2))
        love_score = random.randint(50, 100)
        st.write(f"❤️ **{name1}**님과 **{name2}**님의 궁합 점수는... **{love_score}점**입니다!")

st.title("🔢 내 손안의 스마트 종합 계산기")
st.markdown("사칙연산부터 생활 계산, 방정식, 무작위 뽑기까지 한곳에서 해결하세요!")

st.divider()

# --- 메인 기능 선택 탭 ---
# 사용자가 쉽게 이동할 수 있도록 직관적인 메뉴 탭으로 구성했습니다.
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🧮 사칙연산", 
    "📊 퍼센트 계산", 
    "⚖️ 단위 변환", 
    "💸 n빵(더치페이)", 
    "📝 방정식 & 랜덤"
])

# --- [Tab 1] 일반 사칙연산 ---
with tab1:
    st.subheader("🧮 일반 사칙연산")
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("첫 번째 숫자", value=0.0, step=1.0, key="main_num1")
    with col2:
        num2 = st.number_input("두 번째 숫자", value=0.0, step=1.0, key="main_num2")

    operator = st.selectbox("연산자 선택", ["더하기 (+)", "빼기 (-)", "곱하기 (×)", "나누기 (÷)"], key="main_op")

    if operator == "더하기 (+)":
        st.success(f"✨ 결과: {num1} + {num2} = **{num1 + num2}**")
    elif operator == "빼기 (-)":
        st.success(f"✨ 결과: {num1} - {num2} = **{num1 - num2}**")
    elif operator == "곱하기 (×)":
        st.success(f"✨ 결과: {num1} × {num2} = **{num1 * num2}**")
    elif operator == "나누기 (÷)":
        if num2 == 0:
            st.error("⚠️ 0으로 나눌 수 없습니다!")
        else:
            st.success(f"✨ 결과: {num1} ÷ {num2} = **{num1 / num2:.4f}**")

# --- [Tab 2] 생활 속 퍼센트 계산 ---
with tab2:
    st.subheader("📊 생활 속 퍼센트 계산")
    p_mode = st.selectbox("계산 방식 선택", ["전체 값의 몇 %는 얼마?", "전체 값에서 일부 값은 몇 %?"], key="pct_mode")
    
    if p_mode == "전체 값의 몇 %는 얼마?":
        total_val = st.number_input("전체 값", value=100.0, step=1.0, key="pct_t1")
        target_pct = st.number_input("구하려는 퍼센트(%)", value=10.0, step=1.0, key="pct_p1")
        st.success(f"✨ 결과: {total_val}의 {target_pct}%는 **{total_val * (target_pct / 100.0):.2f}**입니다.")
        
    elif p_mode == "전체 값에서 일부 값은 몇 %?":
        total_val = st.number_input("전체 값", value=100.0, step=1.0, key="pct_t2")
        part_val = st.number_input("일부 값", value=20.0, step=1.0, key="pct_p2")
        if total_val == 0:
            st.error("⚠️ 전체 값은 0이 될 수 없습니다.")
        else:
            st.success(f"✨ 결과: {total_val}에서 {part_val}은 **{(part_val / total_val) * 100.0:.2f}%**입니다.")

# --- [Tab 3] 척척 단위 변환기 ---
with tab3:
    st.subheader("⚖️ 척척 단위 변환기")
    u_mode = st.selectbox("변환 종류", ["길이 (cm ⇄ inch)", "무게 (kg ⇄ lb)"], key="unit_mode")
    
    if u_mode == "길이 (cm ⇄ inch)":
        direction = st.radio("변환 방향", ["cm ➔ inch", "inch ➔ cm"], key="len_dir")
        val = st.number_input("길이 입력", value=1.0, step=1.0, key="len_in")
        if direction == "cm ➔ inch":
            st.success(f"✨ 결과: {val} cm = **{val * 0.393701:.2f} inch**")
        else:
            st.success(f"✨ 결과: {val} inch = **{val * 2.54:.2f} cm**")
            
    elif u_mode == "무게 (kg ⇄ lb)":
        direction = st.radio("변환 방향", ["kg ➔ lb", "lb ➔ kg"], key="wt_dir")
        val = st.number_input("무게 입력", value=1.0, step=1.0, key="wt_in")
        if direction == "kg ➔ lb":
            st.success(f"✨ 결과: {val} kg = **{val * 2.20462:.2f} lb**")
        else:
            st.success(f"✨ 결과: {val} lb = **{val * 0.453592:.2f} kg**")

# --- [Tab 4] 정산의 신, n빵 계산기 ---
with tab4:
    st.subheader("💸 공평한 n빵(더치페이) 계산기")
    total_money = st.number_input("총 결제 금액 (원)", min_value=0, value=50000, step=1000)
    people_count = st.number_input("총 인원 수 (명)", min_value=1, value=4, step=1)
    
    if people_count > 0:
        dutch_pay = total_money // people_count  # 깔끔하게 떨어지도록 정수 나눗셈
        remainder = total_money % people_count
        
        st.info(f"🏃‍♂️ 1인당 내야 할 금액: **{dutch_pay:,} 원**")
        if remainder > 0:
            st.warning(f"💡 애매하게 남은 **{remainder} 원**은 결제자가 보너스로 내기로 해요! 😉")

# --- [Tab 5] 일차방정식 수식 풀이 및 무작위 수 뽑기 ---
with tab4 if False else tab5:  # 안전한 블록 분리용
    st.subheader("📝 1차 방정식 풀이 ($ax + b = 0$)")
    st.markdown("중학교 수학 시간에 배우는 일차방정식의 해를 구해줍니다.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        a = st.number_input("상수 a 입력 (x의 계수)", value=2.0, step=1.0, key="eq_a")
    with col_b:
        b = st.number_input("상수 b 입력", value=-4.0, step=1.0, key="eq_b")
        
    if a == 0:
        if b == 0:
            st.warning("💡 해가 무수히 많습니다. (모든 숫자가 정답!)")
        else:
            st.error("⚠️ 해가 존재하지 않는 모순된 수식입니다. ($a$에 0이 아닌 수를 넣어주세요!)")
    else:
        # ax + b = 0 -> x = -b/a
        equation_solution = -b / a
        st.success(f"🍀 방정식 ${a}x + ({b}) = 0$의 해는 **$x = {equation_solution:.2f}$** 입니다!")
        
    st.divider()
    
    # --- 🎲 행운의 무작위 수(랜덤) 뽑기 ---
    st.subheader("🎲 무작위 수(랜덤) 뽑기")
    st.markdown("발표자 번호 뽑기나 제비뽑기할 때 사용해 보세요!")
    
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        min_rand = st.number_input("시작 숫자(최소)", value=1, step=1)
    with col_r2:
        max_rand = st.number_input("끝 숫자(최대)", value=30, step=1)
        
    if min_rand > max_rand:
        st.error("⚠️ 시작 숫자가 끝 숫자보다 클 수 없습니다!")
    else:
        if st.button("🎰 행운의 숫자 뽑기"):
            picked_num = random.randint(int(min_rand), int(max_rand))
            st.balloons()  # 축하 효과 펑!
            st.success(f"🎉 당첨된 무작위 숫자는 바로 **[{picked_num}]** 입니다!")
