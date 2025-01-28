import os
import streamlit.components.v1 as components
from typing import List, Callable

_RELEASE = True

if not _RELEASE:
  _component_func = components.declare_component(
      "streamlit_clickable_list",
      url="http://localhost:3001",
  )
else:
  parent_dir = os.path.dirname(os.path.abspath(__file__))
  build_dir = os.path.join(parent_dir, "frontend/build")
  _component_func = components.declare_component("streamlit_clickable_list", path=build_dir)


def clickable_list(names: List[str], on_click: Callable[[str], None], key=None):
  # def _on_change():
  #   print(f"_on_change:")
  selected_name = _component_func(names=names, key=key, default=0,
                                  # on_change=_on_change
                                  )
  if selected_name:
    on_click(selected_name)
