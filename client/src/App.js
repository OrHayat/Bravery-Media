import React from "react";
import Header from "./components/header/Header";
import Navbar from "./components/navbar/Navbar";
import Search from "./components/search/Search";
import Landing from "./components/landing/Landing";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { GlobalStyles } from "./styles/global";
import ResultContextProvider from "./contexts/ResultContext";

function App() {
  return (
    <React.Fragment>
      <Router>
        <GlobalStyles />
        <Navbar />
        <Header />
        <Route path="/" exact component={Landing}></Route>
        <ResultContextProvider>
          <Route path="/movies" render={(props) => <Search {...props} />} />
          <Route path="/books" render={(props) => <Search {...props} />} />
          <Route path="/songs" render={(props) => <Search {...props} />} />
          <Route path="/articles" render={(props) => <Search {...props} />} />
        </ResultContextProvider>
      </Router>
    </React.Fragment>
  );
}

export default App;
