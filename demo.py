import streamlit as st
from streamlit_clickable_list import clickable_list

st.title("ClickableList Sample")

if "clicked" not in st.session_state:
  st.session_state['clicked'] = None

st.header("Sample code:")
st.code("""
col1, col2 = st.columns([1, 1])
with col1:
  def on_click(name: str) -> None:
    print(f"clicked: {name}")
    st.session_state['clicked'] = name

  st.header("Clickable list:")
  clickable_list(["aaa", "bbb", "ccc"], on_click, key="clickable_list")

with col2:
  st.header("Result:")
  if "clicked" in st.session_state:
    st.write(f"Clicked: {st.session_state['clicked'] or 'none'}")

""")

if st.button("Reset", use_container_width=True):
  st.session_state['clicked'] = None
  st.rerun()

st.divider()

col1, col2 = st.columns([1, 1])
with col1:
  def on_click(name: str) -> None:
    print(f"clicked: {name}")
    st.session_state['clicked'] = name

  st.header("Clickable list:")
  clickable_list(["aaa", "bbb", "ccc"], on_click, key="clickable_list")

with col2:
  st.header("Result:")
  if "clicked" in st.session_state:
    st.write(f"Clicked: {st.session_state['clicked'] or 'none'}")
