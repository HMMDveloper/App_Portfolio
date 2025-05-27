import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("image/photo.png")


with col2:
    st.title("Joiner Software Engineer Hamza Hameed")
    content = """
    Hi 
    """
    st.info(content)


content2 = """
Below you can find my projects feel free to contact me 
"""

st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv" , sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])


with col4:
    for index, row in df[10:].iterrows():  # Changed to match col3 range
        st.image(f"image/{row['image']}")