//IMPORT LIB
import React, {Component} from 'react';
// ROUTER
import {BrowserRouter} from 'react-router-dom';
//BOTTOMBAR
import BottomBar from './navmenu/bottombar/BottomBar';
//ROUTES
import Routes from './routes/Routes';
//COOKIE
import {CookiesProvider} from 'react-cookie';
// IMG
import Container from './bootstrap/Container';
import UserProvider from './context/UserProvider';

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
                    </div>
                </BrowserRouter>
            </div>
        );
    }
}

//export a component
export default App;