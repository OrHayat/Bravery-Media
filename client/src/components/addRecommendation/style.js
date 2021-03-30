import styled from "styled-components";
import { fontSizes } from "../../styles/typography";
import { colors } from "../../styles/colors";
import { device } from "../../styles/devices";

export const LabelWrapper = styled.div`
  border: transparent;
  border-radius: 4px;
  padding: 2% 0;
  margin: 0.5% 0;
`;

export const Label = styled.label`
  display: block;
  margin: 1% 0;
  font-size: ${fontSizes.fontS};
`;

export const Input = styled.input`
  display: block;
  border-radius: 4px;
  border: 1px solid ${colors.BORDER_GREY};
  padding: 10px 15px;
  margin-bottom: 10px;
  font-size: ${fontSizes.fontS};
  color: ${({ isSubmit }) =>
    isSubmit ? `${fontSizes.fontL}` : `${fontSizes.fontS}`};
  width: 40%;
  color: ${({ isSubmit }) => (isSubmit ? `${colors.WHITE}` : `inherit`)};
  background-color: ${({ isSubmit }) =>
    isSubmit ? `${colors.MAIN_BLUE}` : `inherit`};
  font-weight: ${({ isSubmit }) => (isSubmit ? `bold` : `inherit`)};
  text-transform: ${({ isSubmit }) => (isSubmit ? `uppercase` : `none`)};
`;

export const StyledButton = styled.button`
  text-decoration: none;
  border: transparent;
  border-radius: 4px;
  margin: 1.5%;
  padding: 2%;
`;

export const ErrorAlert = styled.div`
  color: ${colors.RED};
  font-size: ${fontSizes.fontS2};
  margin: 1.5%;
`;

export const Textarea = styled.textarea`
  width: 80%;
  display: block;
  border-radius: 4px;
  border: 1px solid ${colors.BORDER_GREY};
  padding: 10px 15px;
  margin-bottom: 10px;
  font-size: ${fontSizes.fontS};
  font-family: Roboto;
  min-height: 10vh;
`;

export const Divider = styled.hr`
  border: 0.5px solid ${colors.BORDER_GREY};
  margin: 0.5% 0;
`;
