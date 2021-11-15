import React from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { FormControl, Select, TextField, InputLabel, MenuItem, Stack } from '@mui/material';
import store from '../../../index'
import "./FormScatterPlot.css"

export default function FormScatterPlot() {
  
  // Maybe this may work as well ===> const dispatch = useDispatch(store);

  const data = useSelector((state) => state);

  const handlechange = (event) => {
    const { name, value } = event.target
    console.log(name)
    console.log(value)
    if (name == "league") {
      store.dispatch({type: "league_and_read_new", payload: value})
    } else {
      store.dispatch({type: name, payload: value})
    }
  };

  const SelectOptionStyles = {
    backgroundColor: 'white',
    '& label': {
      color: 'white',
    }
  };

  const InputBoxStyles = {
    backgroundColor: 'white',
    '& label.Mui-focused': {
      color: 'green',
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

  return (
  <Stack spacing={2}>
    <h1 style={{ color: 'blue'}}>Customizations</h1>
    <Stack direction="row" spacing={2}>
      <InputLabel id="demo-simple-select-autowidth-label">Choose League</InputLabel>
      <Select
          labelId="demo-simple-select-autowidth-label"
          id="demo-simple-select-autowidth-id"
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
      <InputLabel id="demo-simple-select-autowidth-label-xaxis">Choose League</InputLabel>
      <Select
          labelId="demo-simple-select-autowidth-label-xaxis"
          id="demo-simple-select-autowidth-id"
          name="x_metric"
          value={data.x_metric}
          label="X metric"
          style={SelectOptionStyles}
          onChange={handlechange}>
        <MenuItem value="goals">Goals</MenuItem>
        <MenuItem value="assists">Assists</MenuItem>
        <MenuItem value="npxg">NPXG</MenuItem>
        <MenuItem value="xg_per90">XG_per90</MenuItem>
        <MenuItem value="xa_per90">XA_per90</MenuItem>
        <MenuItem value="xg_xa_per90">XG_XA_per90</MenuItem>
        <MenuItem value="npxg_per90">NPXG_per90</MenuItem>
        <MenuItem value="npxg_xa_per90">NPXG_XA_per90</MenuItem>
      </Select>
      <InputLabel id="demo-simple-select-autowidth-label-yaxis">Choose League</InputLabel>
      <Select
          labelId="demo-simple-select-autowidth-label-yaxis"
          id="demo-simple-select-autowidth-id"
          name="y_metric"
          value={data.y_metric}
          style={SelectOptionStyles}
          label="Y metric"
          onChange={handlechange}>
        <MenuItem value="goals">Goals</MenuItem>
        <MenuItem value="assists">Assists</MenuItem>
        <MenuItem value="npxg">NPXG</MenuItem>
        <MenuItem value="xg_per90">XG_per90</MenuItem>
        <MenuItem value="xa_per90">XA_per90</MenuItem>
        <MenuItem value="xg_xa_per90">XG_XA_per90</MenuItem>
        <MenuItem value="npxg_per90">NPXG_per90</MenuItem>
        <MenuItem value="npxg_xa_per90">NPXG_XA_per90</MenuItem>
      </Select>
    </Stack>    
    <Stack spacing={2}>
      <TextField label="Title" variant="filled"  name="title" value={data.title} onChange={handlechange} style={InputBoxStyles} />
      <TextField label="X-axis" variant="filled" name="xlabel" value={data.xlabel} onChange={handlechange} style={InputBoxStyles}/>
      <TextField label="Y-axis" variant="filled" name="ylabel" value={data.ylabel} onChange={handlechange} style={InputBoxStyles} />
    </Stack>
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
  