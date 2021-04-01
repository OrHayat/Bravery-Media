import React, { useContext, useState, useEffect } from "react";
import axios from "axios";
import clsx from "clsx";
import { ResultContext } from "../../contexts/ResultContext";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import CardMedia from "@material-ui/core/CardMedia";
import CardContent from "@material-ui/core/CardContent";
import CardActions from "@material-ui/core/CardActions";
import Collapse from "@material-ui/core/Collapse";
import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import ResultCard from "../resultCard/ResultCard";
import { Container } from "./style";

const URL = "https://randomuser.me/api/?results=2";

const useStyles = makeStyles((theme) => ({
  root: {
    maxWidth: 345,
    fontFamily: "Roboto",
  },
  media: {
    /* paddingTop: "21.1875%", // 16:9 */
    height: "15vh",
    /*     width: "15vw", */
    backgroundSize: "contain",
  },
  expand: {
    transform: "rotate(0deg)",
    marginLeft: "auto",
    transition: theme.transitions.create("transform", {
      duration: theme.transitions.duration.shortest,
    }),
  },
  expandOpen: {
    transform: "rotate(180deg)",
  },
}));

export default function SearchResult({ item, bookData }) {
  const { resultOpen } = useContext(ResultContext);
  const [imgData, setImageData] = useState("");
  const [resultCard, setResultCard] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  console.log(item);

  const classes = useStyles();
  const [expanded, setExpanded] = useState(false);

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  const handleResultClick = () => {
    setResultCard(true);
  };

  /*   useEffect(() => {
    const fetchData = async () => {
      try {
        setIsLoading(true);
        const result = await axios(URL);
        setImageData(result.data.results[0].picture.medium);
        console.log("data as img: ", imgData);
        setIsLoading(false);
      } catch (err) {
        console.log("err: ", err);
      }
    };

    fetchData();
    return () => setIsLoading(false);
  }, []); */

  return (
    <div>
      {resultCard && (
        <ResultCard item={item} resultOpen={resultOpen} bookData={bookData} />
      )}

      <Container>
        <Card className={classes.root}>
          <CardHeader title={item.title} style={{ textAlign: "center" }} />
          {!isLoading && item.image && (
            <CardMedia
              className={classes.media}
              image={item.image}
              title={item.title}
            />
          )}
          <CardContent>
            <Typography variant="body2" color="textSecondary" component="p">
              Type: {item.type}
            </Typography>
            {item.creator && (
              <Typography variant="body2" color="textSecondary" component="p">
                Creator: {item.creator}
              </Typography>
            )}

            {item.braveryRate ? (
              <Typography variant="body2" color="textSecondary" component="p">
                Bravery Rate: {item.braveryRate}
              </Typography>
            ) : (
              <Typography variant="body2" color="textSecondary" component="p">
                Bravery Rate: Be the first one to rate!
              </Typography>
            )}
          </CardContent>
          <CardActions disableSpacing>
            <ResultCard item={item} bookData={bookData} />
            <IconButton
              className={clsx(classes.expand, {
                [classes.expandOpen]: expanded,
              })}
              onClick={handleExpandClick}
              aria-expanded={expanded}
              aria-label="show more"
            >
              <ExpandMoreIcon />
              <Typography>Plot</Typography>
            </IconButton>
          </CardActions>
          <Collapse in={expanded} timeout="auto" unmountOnExit>
            <CardContent>
              <Typography paragraph style={{ fontSize: "14px" }}>
                {item.plot}
              </Typography>
            </CardContent>
          </Collapse>
        </Card>
      </Container>
    </div>
  );
}
