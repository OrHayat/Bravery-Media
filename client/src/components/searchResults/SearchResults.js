import React from "react";
import { Grid } from "./style";
import SearchResult from "../searchResult/SearchResult";

const SearchResults = ({ searchResults, bookData }) => {
  return (
    <Grid>
      {searchResults.map((item) => (
        <SearchResult item={item} key={item.id} bookData={bookData} />
      ))}
    </Grid>
  );
};

export default SearchResults;
