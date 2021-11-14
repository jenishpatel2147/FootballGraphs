import axios from "axios";

const api =  "http://localhost:8000/";

class scatterplot {
    getplot(league, per90stat, xlabel, ylabel, title, read_new, x_metric, y_metric) {
        const res = axios.get(api + 'api/', 
        { params: {
            league: league,
            per90s: per90stat,
            xlabel: xlabel, 
            ylabel: ylabel, 
            title: title, 
            read_new: read_new,
            x_metric: x_metric,
            y_metric: y_metric
        }});
        return res;
    }
}

export default new scatterplot;
