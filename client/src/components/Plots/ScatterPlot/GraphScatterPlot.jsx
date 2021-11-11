import React, { useEffect, useState } from 'react'
import { Container, Row, Col } from "react-bootstrap";
import scatterplot from "../../../services/scatterplot";
import InnerHTML from 'dangerously-set-html-content'
import { useSelector, useDispatch } from 'react-redux'
import { forminput } from '../../../features/ScatterReducer.js'

const GraphScatterPlot = () => {

    const data = useSelector((state) => state.scatterplot.value);

    const dispatch = useDispatch();
        
    useEffect(() => {
        let isMounted = true;     // note mutable flag
        console.log(data.league);
        scatterplot.getplot(data.league, data.per90s)
        .then((response) => {
            console.log(response.data);
            const resdata = response.data
            dispatch(forminput({
                league: data.league, per90s: data.per90s,
                        title: "Title", xlabel: "x label", ylabel: "y label",
                    current_graph: resdata}, "ALL"));
            console.log("error");
        }).catch((error) => {
            alert(error);
            console.log(error);
        })    
        return () => {isMounted = false};
    }, [dispatch, data.league]);

    const data2 = useSelector((state) => state.scatterplot.value);

    console.log("Getting Values")

    return (<div><InnerHTML html={data2.current_graph} /></div>
    )
}

export default GraphScatterPlot;