import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! OMG!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Streamlit 앱 제목 설정
st.title("버튼 클릭 시 메시지 출력 예제")

# 버튼 추가 (버튼 텍스트는 '메시지 보기')
if st.button("메시지 보기"):
    # 버튼이 클릭되었을 때 출력할 메시지
    st.success("버튼이 눌렸습니다! 여기에 원하는 메시지를 넣으세요.")
else:
    st.write("버튼을 눌러 메시지를 확인해보세요.")

