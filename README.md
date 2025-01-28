# streamlit-clickable-list

See demo: https://demopy-6aplg2asvytivaazchhqbj.streamlit.app/

## How to install
```
pip install streamlit-clickable-list
```

## How to use

```python
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

```

![streamlit-clickable-list_demo](./streamlit-clickable-list_demo.gif)

## For the component development

Based on: https://docs.streamlit.io/develop/concepts/custom-components/intro

### Set up

- Set up python environment and dependencies
  - Used: v3.9
  - If you use `uv`, run:
    ```
    uv sync
    ```
- Set up Node.js environment
  - Used v22.13.1
  - If you use `nvm`, run:
    ```
    nvm use
    ```
- Set up node_modules
  ```
  cd frontend
  npm install
  ```

### Run dev

- Use dev mode
  - Edit `streamlit_clickable_list/__init__.py`
    ```diff
    -_RELEASE = True
    +_RELEASE = False
    ```
- Run dev server
  ```
  cd frontend
  npm start
  ```
- Run streamlit app
  ```
  streamlit run demo.py

  # with WSL
  streamlit run demo.py --server.fileWatcherType=poll --server.address=0.0.0.0
  ```
  - If you use `uv`, add `uv run`

### Release to PyPI

- Use release mode
  - Edit `streamlit_clickable_list/__init__.py`
    ```diff
    -_RELEASE = False
    +_RELEASE = True
    ```
- Build react app
  ```
  cd frontend
  npm build
  ```
- Run the app to check it in local
  ```
  streamlit run demo.py

  # with WSL
  streamlit run demo.py --server.fileWatcherType=poll --server.address=0.0.0.0
  ```
- Build python
  - If you use `uv`, run:
    ```
    uv build
    ```
- Push to GitHub (if you update `README.md`)
- Publish to PyPI
  ```
  uv publish --token <PyPI token>
  ```
  - Check `$HOME/.pypirc` for \<PyPI token\>

### Release to Streamlit Community Cloud

Only the first time:
- Log in [Streamlit Community Cloud](https://streamlit.io/cloud)
- "Create app" > "Deploy a public app from GitHub"
- Input info in "Deploy an app"

To publish:
- First, publish it to PyPI
  - Because the app in Streamlit Community Cloud uses the streamlit-clickable-list in PyPI
- Generate `requirement.txt`
  - If you use `uv`, run:
    ```
    uv pip compile pyproject.toml > requirements.txt
    ```
- Push github, then it will be deployed to Streamlit Community Cloud

