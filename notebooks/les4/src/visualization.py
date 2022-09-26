import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def boxplots(p, target):
    fig, ax = plt.subplots()
    sns.boxplot(data = p.to_pandas(), x = 'variable', y='norm', hue=target, ax=ax)
    st.pyplot(fig)

def pairplot(df, target):
    fig = sns.pairplot(df, hue=target)
    st.pyplot(fig)