import React, { useEffect, useState } from 'react'
import { Container, Row, Col } from "react-bootstrap";
import scatterplot from "../../services/scatterplot";
import  {useSelector, useDispatch} from 'react-redux'
import InnerHTML from 'dangerously-set-html-content'

const Scatter = () => {
    
    const [data, setData] = useState([]);

    console.log("HERE")

    //const getplot = async () => {}
    
    useEffect(() => {
        let isMounted = true;     // note mutable flag
        scatterplot.getplot()
        .then((response) => {
            console.log(response.data);
            if (isMounted) setData(response.data);
            else console.log("NOT MOUNTED - SO NO ATA")
        }).catch((error) => {
            alert(error);
            console.log(error);
        })    
        return () => {isMounted = false};
    }, []);

    console.log("Getting Values")

    return (
            <Container fluid>
                <Row>
                    Hi, I'm some kid trying to learn to code
                </Row>
                <Row>
                <div>
                    <InnerHTML html={data} />
                </div>
                </Row>
            </Container>
    )
}

export default Scatter