import axios from 'axios';

export default axios.create({
    responseType: 'json',
    baseURL: 'http://127.0.0.1:5000/api/0.1'
});