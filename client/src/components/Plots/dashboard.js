import React from 'react'
//import Header from "../Header/Header";
import { Container, Row, Col } from "react-bootstrap";
import FormScatterPlot from './ScatterPlot/FormScatterPlot'
import GraphScatterPlot from "./ScatterPlot/GraphScatterPlot";

export default class Dashboard extends React.Component {
    // eslint-disable-next-line no-useless-constructor
    constructor(props) {
        super(props);
    };

    render() {
        return (
            <Container fluid>
            <Row>
                Hi, I'm some kid trying to learn to code
                <h1>SOME MAGIC SHIT</h1>
            </Row>
            <Row> 
                <Col>
                    <GraphScatterPlot />
                </Col>
                <Col>
                    <FormScatterPlot />
                </Col>    
            </Row>       
            </Container>
        )
    }
}