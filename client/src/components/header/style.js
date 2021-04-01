import styled from "styled-components";
import { fontSizes } from "../../styles/typography";
import { colors } from "../../styles/colors";
import { device } from "../../styles/devices";

export const H1Element = styled.h1`
  font-size: 40px;
  letter-spacing: 0.8;
  font-weight: bold;
  margin: 0;
  text-align: center;
  color: ${colors.DARK_BLUE};

  @media ${device.mobileS} {
  }

  @media ${device.mobileL} {
  }
`;

export const Logo = styled.img`
  height: 9vh;
  width: 16vw;
  margin: 1%;

  @media ${device.mobileS} {
    height: 5vw;
    width: 10vw;
  }

  @media ${device.tablet} {
    height: 5vw;
    width: 10vw;
  }

  @media ${device.laptop} {
    height: 9vh;
    width: 16vw;
  }
`;
