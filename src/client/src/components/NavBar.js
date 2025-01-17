import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import IconButton from "@material-ui/core/IconButton";
import MenuIcon from "@material-ui/icons/Menu";
import { Link } from "react-router-dom";
import MenuItem from "@material-ui/core/MenuItem";
import Divider from '@material-ui/core/Divider';

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
          <Divider className={classes.divider} orientation="vertical" />
          <Typography variant="h7" className={classes.title}>
            <Link to="/Upload" style={{ textDecoration: "none" }}>
              <MenuItem style={{ paddingLeft: 13, color: "white" }}>
                Upload
              </MenuItem>
            </Link>
          </Typography>
          <Divider className={classes.divider} orientation="vertical" />
          <Typography variant="h7" className={classes.title}>
            <Link to="/WebScraping" style={{ textDecoration: "none" }}>
              <MenuItem style={{ paddingLeft: 13, color: "white" }}>
                Web Scraping
              </MenuItem>
            </Link>
          </Typography>
          <Divider className={classes.divider} orientation="vertical"/>
          <Typography variant="h7" className={classes.title}>
            <Link to="/AboutUs" style={{ textDecoration: "none" }}>
              <MenuItem style={{ paddingLeft: 13, color: "white" }}>
                About Us
              </MenuItem>
            </Link>
          </Typography>
        </Toolbar>
      </AppBar>
    </div>
  );
}
