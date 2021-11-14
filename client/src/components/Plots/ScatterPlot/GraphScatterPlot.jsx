import React, { useEffect, useState } from 'react'
import { Container, Row, Col } from "react-bootstrap";
import scatterplot from "../../../services/scatterplot";
import InnerHTML from 'dangerously-set-html-content'
import { useSelector, useDispatch } from 'react-redux'
import store from '../../../index.js'

const GraphScatterPlot = () => {

    const data = useSelector((state) => state);

    //const dispatch = useDispatch();
        
    useEffect(() => {
        let isMounted = true;     // note mutable flag
        console.log(data.league)
        scatterplot.getplot(data.league, data.per90s, data.xlabel, data.ylabel, data.title, data.read_new, data.x_metric, data.y_metric)
        .then((response) => {
            const resdata = response.data
            store.dispatch({type: "graph", payload: resdata});
        }).catch((error) => {
            alert(error);
            console.log(error);
        })    
        return () => {isMounted = false};
    }, [store.dispatch, data.league, data.per90s, data.xlabel, data.ylabel, data.title, data.read_new, data.x_metric, data.y_metric]);

    const data2 = useSelector((state) => state);

    return (<div><InnerHTML html={data2.current_graph} /></div>)
}

export default GraphScatterPlot;