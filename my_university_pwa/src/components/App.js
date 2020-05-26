//import lib
import React, {Component} from 'react';
// ROUTER
import {BrowserRouter} from 'react-router-dom';
// NAVBAR
import Navigation from './navabar/Navigation';
import Navitem from './navabar/Navitem';

//create a component 
class App extends Component {
    render(){
        return (
            <diV>
                <BrowserRouter>
                    <Navigation className='navbar navbar-expand-lg  navbar-dark bg-primary' brandName='myUniversity'>
                        <Navitem path='/' name='News' exact='true'/>
                        <Navitem path='/calendario' name='Calendario'/>
                        <Navitem path='/ricevimento' name='Ricevimento'/>
                        <Navitem path='/chat' name='Chat'/>
                    </Navigation>
                </BrowserRouter>
            </diV>
        );
    }
}

//export a component
export default App;