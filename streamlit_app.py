import streamlit as st
import pandas as pd
import numpy as np

st.title('Dit is een testje van Robert')

st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))

# Display a chat input widget.
st.chat_input("Say something")