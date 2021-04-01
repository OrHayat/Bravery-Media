import React from "react";
import Stepper from "../stepper/Stepper";
import { H1Element } from "./style";

const Landing = () => {
  return (
    <div>
      <H1Element>What you need to do?</H1Element>
      <Stepper />
      {/* <H1Element>Recommended</H1Element> */}
    </div>
  );
};

export default Landing;
