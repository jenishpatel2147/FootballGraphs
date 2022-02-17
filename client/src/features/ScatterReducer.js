import { combineReducers } from 'redux'

const initialStates = {league: "england", per90s: 5, position:"att",
title: "Graph Creator", xlabel: "Goals Per 90", ylabel: "Assits Per 90",
current_graph: {}, read_new: true, x_metric : "goals_per90", y_metric: "assists_per90", display_names : false,
submit: true} 

/*
    base : https://fbref.com/
    playerLink: /en/players/507c7bdf/Bruno-Fernandes,
https://fbref.com/en/players/507c7bdf/ + add "scout/11222/" + "Bruno-Fernandes" "-Scouting-Report"

*/

export default function ScatterReducer(state= initialStates, action) {
    console.log(action.type)
    state = {...state, read_new: false}
    switch (action.type) {
        case "graph":
            return state = {...state, current_graph: action.payload};
        case "per90s":
            return state = {...state, per90s: action.payload};
        case "display_names":
            return state = {...state, display_names: action.payload};
        case "position":
            return state = {...state, position:action.payload};
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
        case "submit":
            return state = {...state, submit: action.payload}
        default:
            return state;
    }
}

/* Maybe in the future
export default combineReducers({
    ScatterReducer
});
*/