//import lib
import React, {Component} from 'react';
// ROUTER
import {BrowserRouter} from 'react-router-dom';
// NAVBAR
import Navigation from './navabar/Navigation';
import Navitem from './navabar/Navitem';
import NavLeft from './navabar/NavLeft';
import NavRight from './navabar/NavRight';
//ROUTES
import Routes from './routes/Routes';
//BOOTSTRAP
import RoundImage from './bootstrap/RoundImage';
// IMG
import myUniversityLogo from '../img//svg//graduation-hat.svg';
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
                        <NavRight>
                            <Navitem path='/profilo'>
                                <RoundImage 
                                  path='https://www.lascimmiapensa.com/wp-content/uploads/2019/03/Al-Bano-1.jpg' 
                                  altText='profile image'
                                  width='45px'
                                  height='45px'/>
                            </Navitem>
                        </NavRight>
                        <NavLeft>
                            <Navitem path='/' name='News' exact={true}/>
                            <Navitem path='/calendario' name='Calendario'/>
                            <Navitem path='/ricevimento' name='Ricevimento'/>
                            <Navitem path='/chat' name='Chat'/>
                        </NavLeft>
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