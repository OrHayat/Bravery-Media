import styled from "styled-components";
import { colors } from "../../styles/colors";

export const Item = styled.div`
  display: flex;
  justify-content: left;
  width: 100%;
  padding: 0.5rem;
  &:hover {
    background-color: ${colors.HOVER_COLOR_1}.;
  }
`;

export const Grid = styled.div`
  display: ${({ resultOpen }) => (resultOpen ? "none" : "grid")};
  width: 90%;
  margin: 0 5% 2% 5%;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 2%;
`;
