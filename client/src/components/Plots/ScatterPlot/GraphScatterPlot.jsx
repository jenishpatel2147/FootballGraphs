import React, { useEffect } from 'react'
import scatterplot from "../../../services/scatterplot";
import InnerHTML from 'dangerously-set-html-content'
import { useSelector } from 'react-redux'
import store from '../../../index.js'
import "./GraphScatterPlot.css"

const GraphScatterPlot = () => {

    const data = useSelector((state) => state);

    //const dispatch = useDispatch();  

    useEffect(() => {
        let isMounted = true;     // note mutable flag
        scatterplot.getplot(data.league, data.per90s, data.position, data.xlabel, data.ylabel, 
            data.title, data.read_new, data.x_metric, data.y_metric, data.display_names)
        .then((response) => {
            const resdata = response.data
            store.dispatch({type: "graph", payload: resdata});
        }).catch((error) => {
            alert(error);
            console.log(error);
        })    
        return () => {isMounted = false};
    }, [store.dispatch, data.submit]);

    const data2 = useSelector((state) => state);

    var image = (data2.current_graph);
    // image = image.toString().replace('height="576pt" version="1.1" viewBox="0 0 1008 576" width="1008pt"',
    //                                  'height="400pt" version="1.1" viewBox="0 0 1008 400" width="1008pt"');
                            //  .replace('<path d="M 0 576 L 1008 576 L 1008 0 L 0 0 z"',
                            //           '<path d="M 0 400 L 1008 400 L 1008 0 L 0 0 z"');
    return (<div><InnerHTML html={data2.current_graph}/></div>)
}

export default GraphScatterPlot;

