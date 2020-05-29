//IMPORT LIB
import React, {Component} from 'react';
// ROUTER
import {BrowserRouter} from 'react-router-dom';
//BOTTOMBAR
import BottomBar from './BottomBar';
//ROUTES
import Routes from './routes/Routes';
//COOKIE
import {CookiesProvider} from 'react-cookie';
// IMG
import Container from './bootstrap/Container';
import UserProvider from './context/UserProvider';

//TODO: UPDATE CONTEXT
//create a component 
class App extends Component {
    render(){
        return (
            <div>
                <BrowserRouter>
                    <div>
                        <Container>
                        <CookiesProvider>
                            <UserProvider>
                                <Routes/>
                            </UserProvider>
                        </CookiesProvider>
                        </Container>
                        <BottomBar 
                            firstYear='2020' 
                            lastYear='2020' 
                            authors={['Carlo Lomello','Francesco Mabilia','Vecchio Roberto']}/>
                    </div>
                </BrowserRouter>
            </div>
        );
    }
}

//export a component
export default App;