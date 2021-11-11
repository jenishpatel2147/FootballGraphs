import axios from "axios";

const api =  "http://localhost:8000/";

class scatterplot {
    getplot(league, per90stat) {
        const res = axios.get(api + 'api/', 
        { params: {
            league: league,
            per90s: per90stat
        }});
        console.log(res);
        return res;
    }
}

export default new scatterplot;
