import React from "react";
import {
  ImgElement,
  HeaderWrapper,
  Divider,
  LabelWrapper,
  Label,
  Text,
  RecommendationWrapper,
} from "./style";
import { colors } from "../../styles/colors";
import AddRecommendation from "../addRecommendation/AddRecommendation";
import Dialog from "@material-ui/core/Dialog";
import { withStyles } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import MuiDialogTitle from "@material-ui/core/DialogTitle";
import MuiDialogContent from "@material-ui/core/DialogContent";
import MuiDialogActions from "@material-ui/core/DialogActions";
import IconButton from "@material-ui/core/IconButton";
import CloseIcon from "@material-ui/icons/Close";
import { fontSizes } from "../../styles/typography";

const styles = (theme) => ({
  root: {
    margin: 0,
    padding: theme.spacing(2),
  },
  closeButton: {
    position: "absolute",
    right: theme.spacing(1),
    top: theme.spacing(1),
    color: theme.palette.grey[500],
  },
});

const DialogTitle = withStyles(styles)((props) => {
  const { children, classes, onClose, ...other } = props;
  return (
    <MuiDialogTitle disableTypography className={classes.root} {...other}>
      <Text variant="h6">{children}</Text>
      {onClose ? (
        <IconButton
          aria-label="close"
          className={classes.closeButton}
          onClick={onClose}
        >
          <CloseIcon />
        </IconButton>
      ) : null}
    </MuiDialogTitle>
  );
});

const DialogContent = withStyles((theme) => ({
  root: {
    padding: theme.spacing(2),
  },
}))(MuiDialogContent);

const DialogActions = withStyles((theme) => ({
  root: {
    margin: 0,
    padding: theme.spacing(1),
  },
}))(MuiDialogActions);

const ResultCard = ({ item, bookData }) => {
  // const img = bookData.volumeInfo.imageLinks.thumbnail;
  const [open, setOpen] = React.useState(false);
  console.log(bookData);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <div>
      <Button variant="outlined" color="primary" onClick={handleClickOpen}>
        More info
      </Button>

      <Dialog
        onClose={handleClose}
        aria-labelledby="customized-dialog-title"
        open={open}
        maxWidth="xl"
      >
        <HeaderWrapper>
          {item.image && <ImgElement src={item.image} />}
          <DialogTitle
            id="customized-dialog-title"
            onClose={handleClose}
            style={{
              padding: "1% 0",
              marginRight: "auto",
              color: `${colors.MAIN_BLUE}`,
              fontSize: "2.25rem",
              minWidth: "20vw",
            }}
          >
            {item.title}
          </DialogTitle>
          <RecommendationWrapper>
            <AddRecommendation item={item} />
          </RecommendationWrapper>
        </HeaderWrapper>

        <DialogContent dividers style={{ marginLeft: "0.5%" }}>
          <LabelWrapper>
            <Label>Type:</Label>
            <Text>{item.type}</Text>
          </LabelWrapper>
          <Divider />
          {item.creator && (
            <LabelWrapper>
              <Label>Creator:</Label>
              <Text>{item.creator}</Text>
            </LabelWrapper>
          )}
          <Divider />
          <LabelWrapper>
            <Label>Bravery Rate:</Label>
            {item.braveryRate ? (
              <Text>{item.braveryRate}</Text>
            ) : (
              <Text>Be the first one to rate!</Text>
            )}
          </LabelWrapper>
          <Divider />
          <LabelWrapper>
            <Label>Bravery Moments in the {item.type}:</Label>
            {item.selectedHeroismMoments ? (
              <ul
                style={{
                  listStyleType: "none",
                  margin: 0,
                  padding: "0 0 0 2%",
                }}
              >
                {item.selectedHeroismMoments &&
                  item.selectedHeroismMoments.map((moment, i) => (
                    <li key={i}>{moment}</li>
                  ))}
              </ul>
            ) : (
              <Text>Be the first one to add bravery moments!</Text>
            )}
          </LabelWrapper>
          <Divider />
          <LabelWrapper>
            <Label>Recommendations:</Label>
            {item.recommendations &&
              item.recommendations.map((rec, i) => (
                <Text
                  key={i}
                  style={{ fontSize: `${fontSizes.fontS}`, display: "block" }}
                >
                  {rec}
                </Text>
              ))}
            {!item.recommendations && (
              <Text>Be the first one to recommend!</Text>
            )}
          </LabelWrapper>
          <Divider />
          <LabelWrapper>
            <Label isPlot={true}>Plot:</Label>
            <Text isPlot={true} style={{ fontSize: `${fontSizes.fontS}` }}>
              {item.plot}
            </Text>
          </LabelWrapper>
          <Divider />
          <LabelWrapper>
            <Label>Is it suitable for education purpose?</Label>
            {item.suitableForEducation === true ? (
              <Text>yes</Text>
            ) : (
              <Text>no</Text>
            )}
          </LabelWrapper>
        </DialogContent>
        <DialogActions>
          <span style={{ marginRight: "auto" }}>
            <AddRecommendation item={item} />
          </span>

          <Button
            onClick={handleClose}
            style={{
              color: `${colors.DARK_BLUE}`,
            }}
          >
            Close
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default ResultCard;
//  <Wrapper resultOpen={resultOpen}></Wrapper>
