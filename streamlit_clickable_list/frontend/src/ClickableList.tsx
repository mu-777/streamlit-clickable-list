import {
  Streamlit,
  withStreamlitConnection,
  ComponentProps,
} from "streamlit-component-lib"
import React, { useCallback, useEffect, useMemo, useState, ReactElement } from "react"

function ClickableList({ args, disabled, theme }: ComponentProps): ReactElement {
  const { names, key } = args
  const [focused, setFocused] = useState<string | null>(null);

  useEffect(() => {
    Streamlit.setFrameHeight()
  }, [theme])

  const handleClick = useCallback((name: string) => {
    setFocused(name);    
  }, []);

  useEffect(()=>{
    Streamlit.setComponentValue(focused);
  }, [focused])

  const style = useMemo(() => {
    if (!theme) return {}

    return {
      padding: "10px",
      cursor: "pointer",
      borderRadius: "5px",
      transition: "background-color 0.2s ease",
      color: theme?.textColor || "#1a73e8",
      // backgroundColor: name === focused ? (theme?.primaryColor || "#d0d0ff") : "transparent",
    }
  }, [theme, focused])

  return (
    <div key={key}>
      {names ? names.map((name: string) => (
        <div
          key={`${key}_${name}`}
          onClick={() => handleClick(name)}
          onMouseEnter={(e) => (e.currentTarget.style.backgroundColor = "#e0e0e0")}
          onMouseLeave={(e) => (e.currentTarget.style.backgroundColor = "transparent")}
          style={style}          
        >
          {name}
        </div>
      )) : null}
    </div>
  );
}

export default withStreamlitConnection(ClickableList)
