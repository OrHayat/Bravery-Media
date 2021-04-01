import styled from "styled-components";
import { colors } from "../../styles/colors";
import { fontSizes } from "../../styles/typography";
import IconButton from "@material-ui/core/IconButton";

export const Container = styled.div`
  display: inherit;
`;
// display: ${({ resultOpen }) => (resultOpen ? "none" : "inherit")};
export const Item = styled.div`
  display: flex;
  justify-content: left;
  width: 100%;
  padding: 0.5rem;
  &:hover {
    background-color: #a1ffff;
  }
`;

export const MoreInfoIcon = styled(IconButton)`
  font-size: ${fontSizes.fontM};
  color: ${colors.MAIN_BLUE};
  &:hover {
    border-radius: 5px;
  }
`;

export const ButtonText = styled.span`
  margin-right: 5px;
  font-size: ${fontSizes.fontM};
  color: ${colors.MAIN_BLUE};
`;
