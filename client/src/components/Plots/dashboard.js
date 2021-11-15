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
                Hi, I'm some kid trying to learn to code
                <h1>SOME MAGIC SHIT</h1>
            <ParticlesLoader />
            <Grid container spacing={2}>
                <Grid item xs={6} md={8}>
                    <GraphScatterPlot />
                </Grid>
                <Grid item xs={6} md={4}>
                    <FormScatterPlot />
                </Grid>
            </Grid>
        </Container>
        )
    }
}