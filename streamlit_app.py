import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! OMG!!! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

#===임의의 그래프 그리기===============================================================#
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create some arbitrary data
np.random.seed(42)
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    'Sales': np.random.randint(100, 500, size=5),
    'Expenses': np.random.randint(50, 300, size=5)
}
df = pd.DataFrame(data)

# Streamlit app code
st.title("Weekly Sales and Expenses Data")

# Line chart for Sales and Expenses over the days
st.line_chart(df.set_index('Day'))

# Matplotlib plot
fig, ax = plt.subplots()
ax.plot(df['Day'], df['Sales'], label='Sales', marker='o')
ax.plot(df['Day'], df['Expenses'], label='Expenses', marker='o')
ax.set_xlabel('Day')
ax.set_ylabel('Amount')
ax.set_title('Sales and Expenses Over Days')
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)



# Streamlit 앱 제목 설정
st.title("버튼 클릭 시 메시지 출력 예제")

# 버튼 추가 (버튼 텍스트는 '메시지 보기')
if st.button("메시지 보기"):
    # 버튼이 클릭되었을 때 출력할 메시지
    st.success("버튼이 눌렸습니다! 여기에 원하는 메시지를 넣으세요.")
else:
    st.write("버튼을 눌러 메시지를 확인해보세요.")

