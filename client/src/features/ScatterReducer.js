import { combineReducers } from 'redux'

const initialStates = {league: "england", per90s: 5,
title: "Title", xlabel: "x label", ylabel: "y label",
current_graph: {}, read_new: true, 
x_metric : "npxg", y_metric: "xa_per90"}

export default function ScatterReducer(state= initialStates, action) {
    console.log(action.type)
    switch (action.type) {
        case "graph":
            return state = {...state, current_graph: action.payload};
        case "title":
            return state = {...state, title: action.payload};
        case "xlabel":
            return state = {...state, xlabel: action.payload};
        case "x_metric":
            return state = {...state, x_metric: action.payload};    
        case "ylabel":
            return state = {...state, ylabel: action.payload};
        case "y_metric":
            return state = {...state, y_metric: action.payload};        
        case "league":
            return state = {...state, league: action.payload};
        case "league_and_read_new":
            return state = {...state, league: action.payload, read_new: true};
        default:
            return state;
    }
}

/* Maybe in the future
export default combineReducers({
    ScatterReducer
});
*/