import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import IconButton from "@material-ui/core/IconButton";
import MenuIcon from "@material-ui/icons/Menu";
import { Link } from "react-router-dom";
import Menu from "@material-ui/core/Menu";
import MenuItem from "@material-ui/core/MenuItem";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

export default function NavBar() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <IconButton
            edge="start"
            className={classes.menuButton}
            color="inherit"
            aria-label="menu"
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h7" className={classes.title}>
            <Link to="/Home" style={{ textDecoration: "none" }}>
              <MenuItem style={{ paddingLeft: 13, color: "white" }}>
                Home
              </MenuItem>
            </Link>
          </Typography>
          <Typography variant="h7" className={classes.title}>
            <Link to="/QueryPage" style={{ textDecoration: "none" }}>
              <MenuItem style={{ paddingLeft: 13, color: "white" }}>
                Query Page
              </MenuItem>
            </Link>
          </Typography>
          <Typography variant="h7" className={classes.title}>
            <Link to="/Upload" style={{ textDecoration: "none" }}>
              <MenuItem style={{ paddingLeft: 13, color: "white" }}>
                Upload
              </MenuItem>
            </Link>
          </Typography>
          <Typography variant="h7" className={classes.title}>
            <Link to="/AboutUs" style={{ textDecoration: "none" }}>
              <MenuItem style={{ paddingLeft: 13, color: "white" }}>
                AboutUs
              </MenuItem>
            </Link>
          </Typography>
        </Toolbar>
      </AppBar>
    </div>
  );
}
