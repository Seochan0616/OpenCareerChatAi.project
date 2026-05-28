# applicationTest.py

import streamlit as st
from careernet import search_job
from classifier import classify_question
from memory import update_memory
from prompt_builder import build_prompt
from api_handler import get_ai_response

# -----------------------------
# 기본 설정
# -----------------------------
st.set_page_config(
    page_title="AI 진로상담 시스템",
    page_icon="🎓"
)

st.title("🎓 교육 공공데이터 기반 AI 진로상담 시스템")

st.write("당신의 고민과 방향을 함께 탐색합니다.")

# -----------------------------
# 메모리 초기화
# -----------------------------
if "memory" not in st.session_state:

    st.session_state.memory = {
        "관심사": [],
        "걱정": [],
        "가치": []
    }

# -----------------------------
# 채팅 기록 초기화
# -----------------------------
if "chat_history" not in st.session_state:

    st.session_state.chat_history = []

# -----------------------------
# 이전 채팅 출력
# -----------------------------
for chat in st.session_state.chat_history:

    with st.chat_message(chat["role"]):

        st.write(chat["content"])

# -----------------------------
# 사용자 입력
# -----------------------------
user_input = st.chat_input("질문을 입력하세요")

# -----------------------------
# 질문 입력 시 실행
# -----------------------------
if user_input:

    # 사용자 채팅 출력
    with st.chat_message("user"):

        st.write(user_input)

    # 기록 저장
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })

    # 질문 분류
    question_type = classify_question(user_input)

    # 메모리 업데이트
    st.session_state.memory = update_memory(
        user_input,
        st.session_state.memory
    )

    # 프롬프트 생성
    prompt = build_prompt(
        user_input,
        question_type,
        st.session_state.memory,
        st.session_state.chat_history
    )

    # AI 응답 생성
    ai_response = get_ai_response(prompt)

    # AI 출력
    with st.chat_message("assistant"):

        st.write(ai_response)

    # 기록 저장
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": ai_response
    })

# -----------------------------
# 메모리 확인
# -----------------------------
with st.expander("상담 메모리 보기"):

    st.write(st.session_state.memory)
