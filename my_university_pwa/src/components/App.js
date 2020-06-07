//IMPORT LIB
import React, {Component} from 'react';
// ROUTER
import {BrowserRouter} from 'react-router-dom';
//ROUTES
import Routes from './routes/Routes';
//DRAWERMENU
import DrawerMenu from './navmenu/drawer_menu/DraweMenu';
//CONTEXT
import {UserContext} from './context/UserContext';
//COOKIES
import { Cookies } from 'react-cookie';
// IMG
import Container from './bootstrap/Container';


//create a component 
class App extends Component {
    constructor(props){
        super(props);
        this.cookies = new Cookies();
    }

    logout = () => {
        this.cookies.remove('isAuth');
        this.cookies.remove('matricola_studente');
        this.cookies.remove('password_studente');
        this.cookies.remove('userCookies');

       //UPDATE CONTEXT
        this.context.update({isAuth:!this.context.isAuth});
    }

    render(){
        return (
            <div>
                <BrowserRouter>
                    <div>
                    { this.context.isAuth && <DrawerMenu onLogout={this.logout}/>}
                        <Container className='page-content'>
                                <Routes/>
                        </Container>
                    </div>
                </BrowserRouter>
            </div>
        );
    }
}

App.contextType = UserContext;

//export a component
export default App;