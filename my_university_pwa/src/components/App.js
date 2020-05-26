//import lib
import React, {Component} from 'react';
// ROUTER
import {BrowserRouter} from 'react-router-dom';
// NAVBAR
import Navigation from './navabar/Navigation';
import Navitem from './navabar/Navitem';
//ROUTES
import Routes from './routes/Routes';

//create a component 
class App extends Component {
    render(){
        return (
            <diV>
                <BrowserRouter>
                    <Navigation className='navbar navbar-expand-lg  navbar-dark bg-primary fixed-top' brandName='myUniversity'>
                        <Navitem path='/' name='News' exact={true}/>
                        <Navitem path='/calendario' name='Calendario'/>
                        <Navitem path='/ricevimento' name='Ricevimento'/>
                        <Navitem path='/chat' name='Chat'/>
                    </Navigation>
                    <Routes/>
                </BrowserRouter>
            </diV>
        );
    }
}

//export a component
export default App;