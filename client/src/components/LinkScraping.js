import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import InputBase from '@material-ui/core/InputBase';

const useStyles = makeStyles((theme) => ({
  root: {
    padding: '2px 4px',
    display: 'flex',
    alignItems: 'center',
    width: 400,
  },
  input: {
    marginLeft: theme.spacing(1),
    flex: 1,
  },
  iconButton: {
    padding: 10,
  },
}));

export default function LinkScraping(props) {
  const classes = useStyles();

  return (
    <Paper component="form" className={classes.root}>
      <InputBase
        value = {props.value}
        className={classes.input}
        onChange = {(e) => props.handleChange(e.target.value)}
        placeholder="Masukkan Link"
        inputProps={{ "aria-label": "masukkan link" }}
        onKeyPress={(ev) => props.handleKeyPress(ev)}
      />
      {/* <IconButton type="button" className={classes.iconButton} aria-label="search">
        <SearchIcon />
      </IconButton> */}
    </Paper>
  );
}