import styled from "styled-components";
import { Link } from "react-router-dom";
import { fontSizes } from "../../styles/typography";
import { colors } from "../../styles/colors";
import { device } from "../../styles/devices";

export const StyledLink = styled(Link)`
  text-decoration: none;
  border: none;
  border-radius: 3%;
  background-color: ${({ isActiveRoute }) =>
    isActiveRoute ? `${colors.FOCUS_BLUE}` : `${colors.DARK_BLUE}`};
  cursor: pointer;
  padding: 1.4% 5%;
  margin: 1%;

  &:hover {
    opacity: 0.8;
    border: none;
  }

  &:focus {
    background-color: ${colors.FOCUS_BLUE};
    outline: none;
  }

  @media ${device.mobileS} {
  }

  @media ${device.mobileM} {
  }

  @media ${device.mobileL} {
  }

  @media ${device.laptop} {
  }

  @media ${device.laptopL} {
    padding: 0.7% 5%;
  }
`;

export const LinkTitle = styled.span`
  font-size: ${fontSizes.fontM};
  color: ${colors.WHITE};
  text-align: center;

  @media ${device.mobileS} {
  }

  @media ${device.tablet} {
  }

  @media ${device.laptop} {
  }
`;
