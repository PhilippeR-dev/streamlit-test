import streamlit as st
from streamlit.components.v1 import html

def graphviz_component(dot_source):
    return html('<div><img src="https://your-graphviz-api-url?dot_source=' + dot_source + '"></div>', width=800, height=600)

st.title("Graphviz Visualization in Streamlit")

dot_source = '''
digraph G {
    A -> B
    B -> C
    C -> A
}
'''

st.write("Graphviz visualization:")
st.components.v1.html(graphviz_component(dot_source))
