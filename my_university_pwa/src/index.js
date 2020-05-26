//import lib
import React from 'react';
import ReactDom from 'react-dom';
import App from './components/App';
import * as serviceWorker from './serviceWorker';
// CSS
import './css/index.css';
//COOKIE
import {CookiesProvider} from 'react-cookie';

//export / render a component
ReactDom.render(<CookiesProvider><App/></CookiesProvider>, document.querySelector('#root'));

serviceWorker.register();