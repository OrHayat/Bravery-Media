import React, { createContext, useState } from "react";

export const ResultContext = createContext();

const ResultContextProvider = (props) => {
  const [resultOpen, setResultOpen] = useState(false);

  const onResultClick = () => {
    setResultOpen(!resultOpen);
  };

  return (
    <ResultContext.Provider value={{ resultOpen, onResultClick }}>
      {props.children}
    </ResultContext.Provider>
  );
};

export default ResultContextProvider;
