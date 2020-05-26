import axios from 'axios';

export default axios.create({
    responseType: 'json',
    baseUrl: 'http://localhost:5000/api/0.1'
});