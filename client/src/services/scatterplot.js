import axios from "axios";

const api =  "http://localhost:8000/";

class scatterplot {
    getplot() {
        const res = axios.get(api + 'api/');
        console.log(res);
        return res;
    }
}

export default new scatterplot;
