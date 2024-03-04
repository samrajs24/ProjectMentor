import React from 'react';
import { Button, Typography, TextField } from '@mui/material';
import { makeStyles } from '@mui/styles';

// Define custom styles using makeStyles
const useStyles = makeStyles((theme) => ({
  button: {
    margin: theme.spacing(1),
  },
}));

function MyComponent() {
  // Use custom styles defined above
  const classes = useStyles();

  return (
    <div>
      {/* Material-UI components */}
      <Typography variant="h1" color="primary">
        Welcome to MyComponent
      </Typography>
      <TextField label="Enter your name" variant="outlined" />
      <Button className={classes.button} variant="contained" color="primary">
        Click Me
      </Button>
    </div>
  );
}

export default MyComponent;
