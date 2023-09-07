import pandas as pd
import streamlit as st

df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
st.write(df)

option = st.selectbox("Which number do you like best?", df["first column"])

st.write("You selected: ", option)
