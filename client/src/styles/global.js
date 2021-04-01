import { createGlobalStyle } from "styled-components";
import { colors } from "./colors";

export const GlobalStyles = createGlobalStyle`
  html, body {
    margin: 0;
    padding: 0;
    background-color: ${colors.LIGHT_GREY};
  }
  
  *, *::after, *::before {
    box-sizing: border-box;
  }

  body {
    width: 100%;
    text-rendering: optimizeLegibility;
    font-family: "Roboto", Roboto, -apple-system, BlinkMacSystemFont, "Segoe UI", 
    Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  }
  
  button {
    cursor: pointer;
  }
  `;
