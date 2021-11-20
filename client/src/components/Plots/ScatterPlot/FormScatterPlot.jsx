import React, {useState} from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { FormControl, FormGroup, FormControlLabel, Select, TextField, InputLabel, MenuItem, Stack, Box, Slider, Switch } from '@mui/material';
import store from '../../../index'
import { HexColorPicker } from "react-colorful";

export default function FormScatterPlot() {
  
  // Maybe this may work as well ===> const dispatch = useDispatch(store);

  const data = useSelector((state) => state);

  const handlechange = (event) => {
    let { name, value } = event.target    
    if (name == "display_names") {
        if (data.display_names == true) {
          value = false
        } else {
          value = true
        }
    } else if (name == "league") {
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

  const InputBoxStyles = {
    backgroundColor: '#d3d3d3',
    '& .MuiInputLabel-root': {
      color: '#da4257 !important',
    },
    '& label.Mui-focused': {
      color: 'white',
    },
    '& .MuiInput-underline:after': {
      borderBottomColor: 'white',
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

/*
Implement FlexBox for Color Palatte 
*/
 
  return (
  <Stack spacing={2}>
    <h1 style={{ color: 'pink'}}>Customizations</h1>
    <Box sx={{ display: 'flex', justifyContent: 'space-evenly', p: 1, m: 1, bgcolor: 'background.paper'}}>
    <FormControl variant="filled" sx={{ m: 1, minWidth: 120 }}>
        <InputLabel id="demo-simple-select-filled-label" style={LabelOptionStyles}>League</InputLabel>
        <Select
          labelId="demo-simple-select-filled-label"
          id="demo-simple-select-filled"
          name="league"
          value={data.league}
          label="Choose League"
          style={SelectOptionStyles}
          onChange={handlechange}>
          <MenuItem value="england">EPL</MenuItem>
          <MenuItem value="italy">Serie A</MenuItem>
          <MenuItem value="spain">La Liga</MenuItem>
          <MenuItem value="germany">Bundesliga</MenuItem>
          <MenuItem value="france">Ligue 1</MenuItem>
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
          <MenuItem value="goals_per90">Goals</MenuItem>
          <MenuItem value="assists_per90">Assists</MenuItem>
          <MenuItem value="key_passes_per90">Key Passes</MenuItem>
          <MenuItem value="progressive_passes_per90">Progressive Passes</MenuItem>
          <MenuItem value="through_balls_per90">Through Balls</MenuItem>
          <MenuItem value="pressures_per90">Pressures</MenuItem>
          <MenuItem value="touches_per90">Touches</MenuItem>
          <MenuItem value="nutmegs_per90">Nutmegs</MenuItem>
          <MenuItem value="miscontrols_per90">Miscontrols</MenuItem>
        </Select>
      </FormControl>
      <FormControl variant="filled" sx={{ m: 1, minWidth: 120 }}>
      <InputLabel id="demo-simple-select-filled-label-y-axis" style={LabelOptionStyles}>Y-axis</InputLabel>
          <Select
            labelId="demo-simple-select-filled-label-y-axis"
            id="demo-simple-select-filled"
            name="y_metric"
            value={data.y_metric}
            style={SelectOptionStyles}
            label="Y metric"
            onChange={handlechange}>
          <MenuItem value="goals_per90">Goals</MenuItem>
          <MenuItem value="assists_per90">Assists</MenuItem>
          <MenuItem value="key_passes_per90">Key Passes</MenuItem>
          <MenuItem value="progressive_passes_per90">Progressive Passes</MenuItem>
          <MenuItem value="through_balls_per90">Through Balls</MenuItem>
          <MenuItem value="pressures_per90">Pressures</MenuItem>
          <MenuItem value="touches_per90">Touches</MenuItem>
          <MenuItem value="nutmegs_per90">Nutmegs</MenuItem>
          <MenuItem value="miscontrols_per90">Miscontrols</MenuItem>
          </Select>
      </FormControl>
    </Box>    
    <Stack spacing={2}>
      <TextField label="Title" variant="filled"  name="title" value={data.title} onChange={handlechange} style={InputBoxStyles} disabled/>
      <TextField label="X-axis" variant="filled" name="xlabel" value={data.xlabel} onChange={handlechange} style={InputBoxStyles} disabled/>
      <TextField label="Y-axis" variant="filled" name="ylabel" value={data.ylabel} onChange={handlechange} style={InputBoxStyles} disabled/>
    </Stack>
    <Box sx={{display: 'flex', justifyContent: 'space-evenly', p: 1, m: 1, bgcolor: 'background.paper',}}>
      <FormControl sx={{ m: 1, minWidth: 120 }}>
        <FormGroup>
            <FormControlLabel
              control={<Switch style={SelectBoxStyles} onChange={handlechange} name="display_names" disabled/>}
              label="Names"
            />
        </FormGroup>
      </FormControl>
      <FormControl variant="filled" sx={{ m: 1, minWidth: 120 }}>
        <InputLabel id="demo-simple-select-filled-label-y-axis" style={LabelOptionStyles}>Position</InputLabel>
          <Select
            labelId="demo-simple-select-filled-label-y-axis"
            id="demo-simple-select-filled"
            name="position"
            value={data.position}
            style={SelectOptionStyles}
            label="Position"
            onChange={handlechange} disabled>
          <MenuItem value="att">Att</MenuItem>
          <MenuItem value="mid">Mid</MenuItem>
          <MenuItem value="full">Full</MenuItem>
          <MenuItem value="def">Def</MenuItem>
          <MenuItem value="all">All</MenuItem>
        </Select>
      </FormControl>
      <Slider aria-label="Per 90" name="per90s" color="secondary" defaultValue={4} valueLabelDisplay="auto" step={2} 
              marks min={0} max={20} onChange={handlechange} disabled/>
    </Box>
  </Stack>
  );
}

/*
"games": 10.0,
"games_starts": 9.0,
"minutes": 855.0,
"minutes_90s": 9.5,
"goals": 0.0,
"assists": 0.0,
"goals_pens": 0.0,
"pens_made": 0.0,
"pens_att": 0.0,
"cards_yellow": 1.0,
"cards_red": 0.0,
"goals_per90": 0.0,
"assists_per90": 0.0,
"goals_assists_per90": 0.0,
"goals_pens_per90": 0.0,
"goals_assists_pens_per90": 0.0,
"xg": 0.8,
"npxg": 0.8,
"xa": 0.3,
"npxg_xa": 1.1,
"xg_per90": 0.08,
"xa_per90": 0.04,
"xg_xa_per90": 0.12,
"npxg_per90": 0.08,
"npxg_xa_per90": 0.12,
*/
  