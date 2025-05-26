import streamlit as st

st.title("💯 용호의 외모점수는?")
st.markdown("### 점수를 1~100 사이로 입력하세요:")

score = st.number_input("용호 점수", min_value=1, max_value=100, step=1)

if st.button("제출"):
    if score < 30:
        st.warning("그 점수는 니얼굴! 용호 외모로 다시 입력요망")
    elif score < 60:
        st.warning("잘못 입력했다.")
    elif score < 80:
        st.info("용호 사진 보고 다시 한번 잘 생각해봐")
    elif score < 90:
        st.info("정말 다시 한번 잘 생각해봐")
    else:
        st.success("역시 넌 나밖에 몰라 ❤️")
