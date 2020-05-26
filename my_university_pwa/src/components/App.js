//import lib
import React, {Component} from 'react';
// ROUTER
import {BrowserRouter, Redirect} from 'react-router-dom';
// NAVBAR
import Navigation from './navabar/Navigation';
import Navitem from './navabar/Navitem';
import NavLeft from './navabar/NavLeft';
import NavRight from './navabar/NavRight';
//BOTTOMBAR
import BottomBar from './BottomBar';
//ROUTES
import Routes from './routes/Routes';
//BOOTSTRAP
import RoundImage from './bootstrap/RoundImage';
// IMG
import myUniversityLogo from '../img//svg//graduation-hat.svg';
import Container from './bootstrap/Container';

//create a component 
class App extends Component {

    viewLoad( isloaded ){
        if(isloaded){
            return(
                <div>
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
                    <BottomBar 
                        firstYear='2020' 
                        lastYear='2020' 
                        authors={['Carlo Lomello','Francesco Mabilia','Vecchio Roberto']}/>
                </div>
            )
        }else{
        return(
            <div>
                <Redirect to={{pathname: "/login"}}/>
                <Container>
                    <Routes/>
                </Container>
            </div>);
        }
    }

    render(){
        return (
            <div>
                <BrowserRouter>
                    {this.viewLoad(false)}
                </BrowserRouter>
            </div>
        );
    }
}

//export a component
export default App;