import styled from "styled-components";
import { colors } from "../../styles/colors";
import { fontSizes } from "../../styles/typography";
import { device } from "../../styles/devices";
import Typography from "@material-ui/core/Typography";

export const Wrapper = styled.div``;
// display: ${({ resultOpen }) => (resultOpen ? "flex" : "none")};

export const HeaderWrapper = styled.div`
  display: flex;
  flex-wrap: wrap;
  align-items: center;

  flex-wrap: wrap;
  margin: 2.5%;
`;

export const ImgElement = styled.img`
  height: 15vh;
  width: 10vw;
  margin-right: 2%;

  @media ${device.mobileS} {
    height: 15vh;
    width: 25vw;
  }

  @media ${device.mobileL} {
    height: 15vh;
    width: 25vw;
  }

  @media ${device.tablet} {
    height: 15vh;
    width: 10vw;
  }

  @media ${device.laptop} {
    height: 20vh;
    width: 10vw;
  }
`;

export const RecommendationWrapper = styled.span`
  margin-top: auto;
`;

export const LabelWrapper = styled.div`
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  border: transparent;
  border-radius: 4px;
  padding: 1.5% 0;
  margin: 0.5% 0;
`;

export const Label = styled.label`
  margin-right: 1%;
  font-size: ${fontSizes.fontL};
  color: ${colors.LOGO_BLUE};
  display: ${({ isPlot }) => (isPlot ? "block" : "inherit")};
  width: ${({ isPlot }) => (isPlot ? "100%" : "inherit")};
  line-heigt: ${({ isPlot }) => (isPlot ? "1.5" : "inherit")};
`;

export const Divider = styled.hr`
  border: 0.5px solid ${colors.BORDER_GREY};
  margin: 0.5% 0;
`;

export const Text = styled(Typography)`
  margin-bottom: 0;
  margin-top: 0.25%;
  padding-top: 0.5%;
  padding-left: ${({ isPlot }) => (isPlot ? "0" : "2%")};
  background-color: ${colors.TRANSPARENT};
`;
