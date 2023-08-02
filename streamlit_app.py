import streamlit as st
import graphviz

st.graphviz_chart('''digraph {
    a [shape="ellipse" style="filled" fillcolor="#1f77b4"]
    b [shape="polygon" style="filled" fillcolor="#ff7f0e"]
    a -> b [fillcolor="#a6cee3" color="#1f78b4"]
}
''')
