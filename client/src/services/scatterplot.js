import axios from "axios";

//const api =  "https://livegrapherapi.herokuapp.com/";
const api = "http://localhost:8000/"

class scatterplot {
    getplot(league, per90stat, position, xlabel, ylabel, title, read_new, x_metric, y_metric, display_names) {
    const res = axios.get(api + 'api/', 
        { params: {
            league: league,
            per90s: per90stat,
            position: position,
            xlabel: xlabel, 
            ylabel: ylabel, 
            title: title, 
            read_new: read_new,
            x_metric: x_metric,
            y_metric: y_metric,
            display_names: display_names
        }});
        return res;
    }
}

export default new scatterplot;
