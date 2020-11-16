import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import InputBase from "@material-ui/core/InputBase";
import IconButton from "@material-ui/core/IconButton";
import SearchIcon from "@material-ui/icons/Search";

const useStyles = makeStyles((theme) => ({
  root: {
    padding: "2px 4px",
    display: "flex",
    alignItems: "center",
    width: 400,
  },
  input: {
    marginLeft: theme.spacing(1),
    flex: 1,
  },
  iconButton: {
    padding: 10,
  },
  divider: {
    height: 28,
    margin: 4,
  },
}));

export default function CustomizedInputBase(props) {
  const classes = useStyles();
  return (
    <Paper component="form" className={classes.root}>
      <InputBase
        value = {props.value}
        className={classes.input}
        onChange = {(e) => props.handleChange(e.target.value)}
        placeholder="Search Dokumen"
        inputProps={{ "aria-label": "search dokumen" }}
        onKeyPress={(ev) => props.handleKeyPress(ev)}
      />
      <IconButton
        type="submit"
        className={classes.iconButton}
        aria-label="search"
        href="/QueryPage"
      >
        <SearchIcon />
      </IconButton>
    </Paper>
  );
}
