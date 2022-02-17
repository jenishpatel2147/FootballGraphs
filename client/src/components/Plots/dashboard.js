import React from 'react'
//import Header from "../Header/Header";
import FormScatterPlot from './ScatterPlot/FormScatterPlot'
import GraphScatterPlot from "./ScatterPlot/GraphScatterPlot";
import ParticlesLoader from './Particles';
import { Container, Grid } from '@mui/material';
import "./Dashboard.css"


export default class Dashboard extends React.Component {
    // eslint-disable-next-line no-useless-constructor
    constructor(props) {
        super(props);
    };

    render() {
        return (
        <Container>
            <ParticlesLoader />
            <h1>Graph Generator</h1>
            Hi, I'm a student creating grapsh for stuff that I don't understand.
            <Grid container spacing={16}>
                <Grid item xs={6} md={6} backgroundColor={{color: "white"}}>
                    <GraphScatterPlot />
                </Grid>
                <Grid item xs={6} md={6}>
                    <FormScatterPlot />
                </Grid>
            </Grid>
        </Container>
        )
    }
}