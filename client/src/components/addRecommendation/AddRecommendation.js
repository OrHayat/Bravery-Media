import React, { useState } from "react";
import Button from "@material-ui/core/Button";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogTitle from "@material-ui/core/DialogTitle";
import { useForm } from "react-hook-form";
import { colors } from "../../styles/colors";
import {
  LabelWrapper,
  Label,
  Input,
  StyledButton,
  ErrorAlert,
  Textarea,
  Divider,
  Select,
  RadioWrapper,
  RadioInput,
} from "./style";

export default function AddRecommendation({ item }) {
  const [open, setOpen] = useState(false);
  const { register, errors, handleSubmit } = useForm();
  const [indexes, setIndexes] = useState([]);
  const [counter, setCounter] = useState(0);
  const [selectVal, setSelectVal] = useState();

  const onSubmit = (data) => {
    console.log(data);
    console.log(errors);
    console.log(selectVal);
    if (errors === {} && selectVal !== "") {
      setIndexes([]);
      setCounter(0);
      // organize json data for server
      // send data to server
    }
    setOpen(false);
  };
  console.log("errors", errors);

  const addBraveryMoment = () => {
    setIndexes((prevIndexes) => [...prevIndexes, counter]);
    setCounter((prevCounter) => prevCounter + 1);
  };

  const removeBraveryMoment = (index) => () => {
    setIndexes((prevIndexes) => [
      ...prevIndexes.filter((item) => item !== index),
    ]);
    setCounter((prevCounter) => prevCounter - 1);
  };

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <div>
      <Button
        variant="outlined"
        style={{
          color: `${colors.DARK_BLUE}`,
          backgroundColor: `${colors.GREY}`,
          fontSize: "12px",
        }}
        onClick={handleClickOpen}
      >
        Add a recommendation
      </Button>
      <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="form-dialog-title"
        maxWidth="xl"
      >
        <DialogTitle
          style={{
            padding: "1% 2.5%",
            width: "90vw",
            color: `${colors.DARK_BLUE}`,
          }}
        >
          Recommend the {item.type} "{item.title}"
        </DialogTitle>
        <DialogContent>
          <form onSubmit={handleSubmit(onSubmit)}>
            <LabelWrapper>
              <Label>Name</Label>
              <Input
                type="text"
                name="name"
                placeholder="add your name"
                ref={register({ required: true, maxLength: 80, minLength: 2 })}
              />
              {errors.name && <ErrorAlert>name is required</ErrorAlert>}
            </LabelWrapper>
            <Divider />
            <LabelWrapper>
              <Label>
                Rate the level of bravery of the {item.type} (from 1 to 10)
              </Label>
              <Select
                name="braveryRate"
                ref={register({ required: true })}
                onChange={(e) => setSelectVal(e.currentTarget.value)}
              >
                <option disabled value defaultValue>
                  select a rate level
                </option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
                <option value="10">10</option>
              </Select>
              {errors.braveryRate && (
                <ErrorAlert>please rate the level of bravery</ErrorAlert>
              )}
              {!selectVal && (
                <ErrorAlert>please rate the level of bravery</ErrorAlert>
              )}
            </LabelWrapper>
            <Divider />
            <LabelWrapper>
              <Label>
                Fill the part that reflects the bravery (minutes in movie, page
                numbers in book, line number in article/song)
              </Label>
              {indexes.map((index) => {
                const fieldName = `moments[${index}]`;
                return (
                  <fieldset name={fieldName} key={fieldName}>
                    <Label>Add part (minute/ page number/ line number)</Label>
                    <Input
                      type="number"
                      min="0"
                      name={`${fieldName}.moment`}
                      placeholder="add only numbers please"
                      ref={register({ minLength: 1, pattern: /^[0-9]*$/ })}
                    />
                    <StyledButton
                      type="button"
                      onClick={removeBraveryMoment(index)}
                    >
                      Remove
                    </StyledButton>
                  </fieldset>
                );
              })}

              <StyledButton type="button" onClick={addBraveryMoment}>
                Add a bravery part
              </StyledButton>
              {counter === 0 && (
                <ErrorAlert>Please add a bravery part</ErrorAlert>
              )}
            </LabelWrapper>
            <Divider />
            <LabelWrapper>
              <Label>Why do you think this parts represent bravery acts?</Label>
              <Textarea
                isTextArea={true}
                name="recommendationDesc"
                placeholder="explain why are you recommending this parts"
                ref={register({
                  required: true,
                  maxLength: 300,
                  minLength: 2,
                })}
              />
              {errors.recommendationDesc && (
                <ErrorAlert>please add your recommendation</ErrorAlert>
              )}
            </LabelWrapper>
            <Divider />
            <LabelWrapper>
              <Label>Is it suitable for education purpose?</Label>
              <RadioWrapper>
                <Label>
                  Yes
                  <RadioInput
                    name="suitableForEducation"
                    id="suitableForEducation"
                    type="radio"
                    value="Yes"
                    ref={register({ required: true })}
                  />
                </Label>
              </RadioWrapper>
              <RadioWrapper>
                <Label>
                  No
                  <RadioInput
                    name="suitableForEducation"
                    id="notSuitableForEducation"
                    type="radio"
                    value="No"
                    ref={register({ required: true })}
                  />
                </Label>
              </RadioWrapper>
              {errors.suitableForEducation && (
                <ErrorAlert>please choose an answer</ErrorAlert>
              )}
            </LabelWrapper>
            <Input
              type="submit"
              isSubmit={true}
              style={{ cursor: "pointer" }}
            />
          </form>
        </DialogContent>
        <DialogActions>
          <Button
            onClick={handleClose}
            style={{
              color: `${colors.DARK_BLUE}`,
            }}
          >
            Cancel
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}
