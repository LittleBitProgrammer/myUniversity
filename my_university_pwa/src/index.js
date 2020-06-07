//import lib
import React from 'react';
import ReactDom from 'react-dom';
import App from './components/App';
import * as serviceWorker from './serviceWorker';
//COOKIE
import {CookiesProvider} from 'react-cookie';
//PROVIDER
import UserProvider from './components/context/UserProvider';
// CSS
import './css/index.css';

//export / render a component
ReactDom.render(<UserProvider><CookiesProvider><App/></CookiesProvider></UserProvider>, document.querySelector('#root'));

serviceWorker.register();