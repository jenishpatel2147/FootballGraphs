import React from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { forminput } from '../../../features/ScatterReducer.js'
import { FormControl, Select, TextField, InputLabel, MenuItem } from '@mui/material';
import "./FormScatterPlot.css"

export default function FormScatterPlot(props) {
  const dispatch = useDispatch();

  const data = useSelector((state) => state.scatterplot.value);

  const handlechange = (event) => {
    dispatch(forminput({
      league: event.target.value, per90s: 5,
              title: "title", xlabel: "x label", ylabel: "y label",
          current_graph: data.current_graph
      }))
  };

  return (
    <FormControl class="new">
      <InputLabel id="demo-simple-select-autowidth-label">Choose League</InputLabel>
      <Select
          labelId="demo-simple-select-autowidth-label"
          id="demo-simple-select-autowidth-id"
          value={data.league}
          label="Choose League"
          onChange={handlechange}>
        <MenuItem value="england">EPL</MenuItem>
        <MenuItem value="italy">Serie A</MenuItem>
        <MenuItem value="spain">La Liga</MenuItem>
        <MenuItem value="germany">Bundesliga</MenuItem>
        <MenuItem value="france">Ligue 1</MenuItem>
      </Select>
      <TextField id="outlined-basic" label="Title" variant="outlined" />
      <TextField id="outlined-basic" label="X-axis" variant="outlined" />
      <TextField id="outlined-basic" label="Y-axis" variant="outlined" />
    </FormControl>

  );
}

  