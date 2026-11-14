from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Microbial Fuel Cell Simulator",
    page_icon="🔋",
    layout="wide",
)

# Remove default Streamlit padding so the simulator fills the page
st.markdown(
    "<style>.block-container{padding-top:1rem;padding-bottom:0;max-width:1250px}</style>",
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=1700, scrolling=True)
