import axios from 'axios';

export default axios.create({
    responseType: 'json',
    baseURL: 'https://my-university-api.herokuapp.com/api/0.1'
});