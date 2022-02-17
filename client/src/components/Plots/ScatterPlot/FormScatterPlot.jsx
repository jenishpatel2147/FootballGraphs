import React, {useState} from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { FormControl, FormGroup, FormControlLabel, Select, TextField, Button,
  InputLabel, MenuItem, Stack, Box, Slider, Grid, Switch, createTheme, Typography, ThemeProvider } from '@mui/material';
import store from '../../../index'
import { HexColorPicker } from "react-colorful";
import {menu_items, positions, leagues} from './data';
import './FormScatterPlot.css'

export default function FormScatterPlot() {
  
  // Maybe this may work as well ===> const dispatch = useDispatch(store);

  const data = useSelector((state) => state);

  const handlechange = (event) => {
    let { name, value } = event.target   
    
    if (name === "display_names") {
      if (data.display_names) { value = false } else { value = true}
    } else if (name === "submit") {
      if (data.submit) { value = false } else { value = true}
    } else if (name === "league") {
      name = "league_and_read_new"
    }
    console.log(name)
    console.log(value)
    store.dispatch({type: name, payload: value});
  };


  const SelectOptionStyles = {
    backgroundColor: '#d3d3d3',
  };

  const LabelOptionStyles = {
    color: '#da4257',
    'font-size': '17px',
    'font-family': 'arial', 
    'font-weight': 'bold',
  };
  
  const SelectBoxStyles = {
    color: '#da4257',
    '& .MuiSwitch-root' :{
      color: '#da4257',
    }
  }

  const styles = {
    TextFieldLabelStyle: {
      color: '#da4257 !important'
    }
  }

  const InputBoxStyles = {
    backgroundColor: '#d3d3d3',
    '& .MuiInputLabel-root': {
      color: '#da4257 !important',
    },
    '& .css-au3a9q-MuiFormLabel-root-MuiInputLabel-rootlabel': {
      color: '#da4257 !important',
    },
    '& .MuiInput-underline:after': {
      borderBottomColor: '#da4257 !important',
    },
    '& .MuiOutlinedInput-root': {
      '& fieldset': {
        borderColor: 'white',
      },
      '&:hover fieldset': {
        borderColor: 'lightgreen',
      },
      '&.Mui-focused fieldset': {
        borderColor: 'green',
      },
    },
  };


  const theme = createTheme();

    theme.typography.h3 = {
      fontSize: '1.2rem',
      '@media (min-width:600px)': {
        fontSize: '1.5rem',
      },
      [theme.breakpoints.up('md')]: {
        fontSize: '2.4rem',
      },
    };
    theme.typography.body2 = {
      fontSize: '0.5rem',
      '@media (min-width:600px)': {
        fontSize: '0.5rem',
      },
      [theme.breakpoints.up('md')]: {
        fontSize: '1rem',
      },
    };

/*
Implement FlexBox for Color Palatte 
*/
 
  return (<Grid container direction="row" alignItems="center" justifyContent="center" style={{ minHeight: '100vh' }}> 
            <Grid item md={6} lg={5}>
              <ThemeProvider theme={theme}>
                <Typography variant="h3">Responsive h3</Typography>
                <Typography variant="body2">All statistics are from Fbrer, Last 365 days</Typography>
              </ThemeProvider>
            </Grid> 
            <Grid item md={6} lg={5}>
              <Box sx={{ display: 'flex', justifyContent: 'space-evenly', p: 1, m: 1}}>
                <FormControl variant="filled" sx={{ m: 1, minWidth: 120 }}>
                    <InputLabel id="demo-simple-select-filled-label" style={LabelOptionStyles}>League</InputLabel>
                    <Select labelId="demo-simple-select-filled-label" id="demo-simple-select-filled" name="league"
                        value={data.league} label="Choose League" style={SelectOptionStyles} onChange={handlechange}>
                      {leagues.map(({item, display}) => (<MenuItem value={item}>{display}</MenuItem>))}
                    </Select>
                  </FormControl>
                  <FormControl variant="filled" sx={{ m: 1, minWidth: 120 }}>
                    <InputLabel id="demo-simple-select-filled-label-x-axis" style={LabelOptionStyles}>X-axis</InputLabel>
                      <Select
                        labelId="demo-simple-select-filled-label-x-axis"
                        id="demo-simple-select-filled"
                        name="x_metric"
                        value={data.x_metric}
                        label="X metric"
                        style={SelectOptionStyles}
                        onChange={handlechange}>
                          {menu_items.map(({item, display}) => (<MenuItem value={item}>{display}</MenuItem>))}
                    </Select>
                  </FormControl>
                  <FormControl variant="filled" sx={{ m: 1, minWidth: 120 }}>
                  <InputLabel id="demo-simple-select-filled-label-y-axis" style={LabelOptionStyles}>Y-axis</InputLabel>
                      <Select labelId="demo-simple-select-filled-label-y-axis" id="demo-simple-select-filled"
                        name="y_metric" value={data.y_metric} style={SelectOptionStyles} label="Y metric" onChange={handlechange}>
                        {menu_items.map(({item, display}) => (<MenuItem value={item}>{display}</MenuItem>))}
                      </Select>
                  </FormControl>
                </Box>    
                <Stack spacing={2}>
                  <TextField label="Title" variant="filled"  name="title" value={data.title} onChange={handlechange} 
                  className={styles.TextFieldLabelStyle}
                  style={InputBoxStyles}/>
                  <TextField label="X-axis" variant="filled" name="xlabel" value={data.xlabel} onChange={handlechange} style={InputBoxStyles}/>
                  <TextField label="Y-axis" variant="filled" name="ylabel" value={data.ylabel} onChange={handlechange} style={InputBoxStyles}/>
                </Stack>
                <Box sx={{ display: 'flex', justifyContent: 'space-evenly', p: 1, m: 1}}>
                  <FormControl sx={{ m: 1, minWidth: 120 }}>
                    <FormGroup>
                        <FormControlLabel
                          control={<Switch style={SelectBoxStyles} onChange={handlechange} name="display_names"/>}
                          label="Logos"
                        />
                    </FormGroup>
                  </FormControl>
                  <FormControl variant="filled" justifyContent='space-evenly' sx={{ m: 1, minWidth: 120 }}>
                    <InputLabel id="demo-simple-select-filled-label-y-axis" style={LabelOptionStyles}>Position</InputLabel>
                      <Select
                        labelId="demo-simple-select-filled-label-y-axis"
                        id="demo-simple-select-filled"
                        name="position"
                        value={data.position}
                        style={SelectOptionStyles}
                        label="Position"
                        onChange={handlechange}>
                          {positions.map(({item, display}) => (<MenuItem value={item}>{display}</MenuItem>))}
                    </Select>
                    <Slider aria-label="Per 90" name="per90s" color="secondary" defaultValue={4} valueLabelDisplay="auto" step={2} marks min={0} max={20} onChange={handlechange}/>
                  </FormControl>

                </Box>
            </Grid>
            <Grid item lg={10}>
              <FormControl sx={{ m: 1, minWidth: 120 }}>
                <Button name="submit" className='' onClick={handlechange}>Generate Graph</Button>
              </FormControl>
            </Grid>
  </Grid>
  );
}
  