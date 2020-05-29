//import lib
import React from 'react';
import ReactDom from 'react-dom';
import App from './components/App';
import * as serviceWorker from './serviceWorker';
// CSS
import './css/index.css';

//export / render a component
ReactDom.render(<App/>, document.querySelector('#root'));

serviceWorker.register();