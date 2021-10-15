import React from 'react'
//import Header from "../Header/Header";
import Scatter from "./chartdisplay";
import Userinput from './userinput';

export default class Dashboard extends React.Component {
    // eslint-disable-next-line no-useless-constructor
    constructor(props) {
        super(props);
    };

    render() {
        return (
            <div>
                <h1>SOME MAGIC SHIT</h1>
                <Scatter />
                <Userinput />
            </div>
        )
    }
}