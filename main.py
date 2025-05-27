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

col3, empty_col ,col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv" )

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("image/" +row["image"])
        st.write("[Source Code](https://pythonhow.com) ")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("image/" + row["image"])
        st.write("[Source Code](https://pythonhow.com) ")