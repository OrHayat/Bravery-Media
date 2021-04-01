import styled from "styled-components";
import { fontSizes } from "../../styles/typography";
import { colors } from "../../styles/colors";
import { device } from "../../styles/devices";

export const H1Element = styled.h1`
  font-size: ${fontSizes.fontXL};
  letter-spacing: 0.8;
  font-weight: bold;
  margin-top: 5%;
  text-align: center;
  color: ${colors.LOGO_BLUE};

  @media ${device.mobileS} {
  }

  @media ${device.mobileL} {
  }
`;
