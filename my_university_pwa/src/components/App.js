//import lib
import React, {Component} from 'react';
// ROUTER
import {BrowserRouter} from 'react-router-dom';
// NAVBAR
import Navigation from './navabar/Navigation';
import Navitem from './navabar/Navitem';
//ROUTES
import Routes from './routes/Routes';
// IMG
import myUniversityLogo from '../img//svg//graduation-hat.svg'
import Container from './bootstrap/Container';

//create a component 
class App extends Component {
    render(){
        return (
            <div>
                <BrowserRouter>
                    <Navigation 
                      className='navbar navbar-expand-lg navbar-dark bg-primary fixed-top' 
                      brandName='myUniversity' 
                      logoPath={myUniversityLogo}>
                        <Navitem path='/' name='News' exact={true}/>
                        <Navitem path='/calendario' name='Calendario'/>
                        <Navitem path='/ricevimento' name='Ricevimento'/>
                        <Navitem path='/chat' name='Chat'/>
                    </Navigation>
                    <Container>
                        <Routes/>
                    </Container>
                </BrowserRouter>
            </div>
        );
    }
}

//export a component
export default App;