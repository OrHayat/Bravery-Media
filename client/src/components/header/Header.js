import React, { Fragment } from "react";
import logo from "../../assets/logo.png";
import { Logo } from "./style";

import { H1Element } from "./style";

const Header = () => {
  return (
    <Fragment>
      <Logo src={logo} />
      <H1Element>Bravery Media</H1Element>
    </Fragment>
  );
};

export default Header;
