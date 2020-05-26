//import lib
import React, {Component} from 'react';
// ROUTER
import {BrowserRouter} from 'react-router-dom';
// NAVBAR
import Navitem from './navabar/Navitem';
import Toggler from './navabar/Toggler';

//create a component 
class App extends Component {
    render(){
        return (
            <diV>
                <BrowserRouter>
                    <nav className="navbar navbar-expand-lg  navbar-dark bg-primary">
                        <a className="navbar-brand" href="/">Navbar</a>
                        <Toggler/>

                        <div className="collapse navbar-collapse" id="navbarSupportedContent">
                            <ul className="navbar-nav mr-auto">
                                <Navitem path='/' name='News' exact='true'/>
                                <Navitem path='/calendario' name='Calendario'/>
                                <Navitem path='/ricevimento' name='Ricevimento'/>
                                <Navitem path='/chat' name='Chat'/>
                            </ul>
                        </div>
                    </nav>
                </BrowserRouter>
            </diV>
        );
    }
}

//export a component
export default App;