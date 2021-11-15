import React from 'react'
//import Header from "../Header/Header";
import FormScatterPlot from './ScatterPlot/FormScatterPlot'
import GraphScatterPlot from "./ScatterPlot/GraphScatterPlot";
import ParticlesLoader from './Particles';
import { Grid, Container } from '@mui/material';


export default class Dashboard extends React.Component {
    // eslint-disable-next-line no-useless-constructor
    constructor(props) {
        super(props);
    };

    render() {
        return (
        <Container fluid>
            <ParticlesLoader />
            Hi, I'm some kid trying to learn to code
            <h1>SOME MAGIC SHIT</h1>
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