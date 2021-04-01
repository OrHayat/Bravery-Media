import React from "react";
import { useLocation } from "react-router-dom";
import { StyledLink, LinkTitle } from "./style";

const Link = (props) => {
  const location = useLocation();

  return (
    <StyledLink to={props.to} isActiveRoute={props.to === location.pathname}>
      {props.children}
      {props.name && <LinkTitle>{props.name}</LinkTitle>}
    </StyledLink>
  );
};

export default Link;
