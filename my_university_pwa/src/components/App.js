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
//COOKIE
import {Cookies, withCookies} from 'react-cookie';
import {instanceOf} from 'prop-types';
//AXIOS
import myUniversity from '../API/myUniversity';
import Loading from './pages/Loading';

//create a component 
class App extends Component {
    static propTypes = {
        cookies: instanceOf(Cookies).isRequired
      };

    constructor(props){
        super(props);
        this.myCookies = new Cookies();
        const {cookies} = props;

        this.state={
            matricola_studente: cookies.get('matricola_studente') || '',
            matricola_docente: cookies.get('matricola_docente') || '',
            password_studente: cookies.get('password_studente') || '',
            password_docente: cookies.get('password_docente') || '',
            isLoading: true
        }
    }

    logout = () => {
        this.myCookies.remove('isAuth');
        this.myCookies.remove('matricola_studente');
        this.myCookies.remove('password_studente');
        this.myCookies.remove('userCookies');

       //UPDATE CONTEXT
        this.context.update({isAuth:!this.context.isAuth});
    }

    login = async() => {
        console.log('entrato in login')
        let response;
        let userType;
        let isAuth;

        try{
            response = await myUniversity.post('/student/login', {
                matricola_studente: this.state.matricola_studente,
                password_studente: this.state.password_studente
            });
        }catch(error){
            console.log(`😱 There was an error: ${error}`);
            isAuth = false;
        }
        if (response.data.length !== 0){
            isAuth = true;
            userType = 'student';
        }else{
            try{
                response = await myUniversity.post('/professor/login',{
                    matricola_docente: this.state.matricola_docente,
                    password_docente: this.state.password_docente
                });
            }catch(error){
                console.log(`😱 There was an error: ${error}`);
                isAuth = false;
            }

            if (response.data.length !== 0){
                isAuth = true;
                userType = 'teacher';
            }else{
               isAuth = false;
            }
        }

        // UPDATE STATE
        this.setState({userType: userType, response:response.data[0], isLoading: false});
        //UPDATE COOKIES
        this.myCookies.set('isAuth',isAuth,{ path: '/' });
        //UPDATE CONTEXT
        this.context.update({[userType]:response.data[0], isAuth: !this.context.isAuth})
    }

    componentDidMount(){
        console.log('app did mount')
        if((this.state.matricola_studente && this.state.password_studente) || 
           (this.state.matricola_docente && this.state.password_docente)){
               this.login();
           }else{
                console.log('sbagliato')
                //UPDATE CONTEXT
                this.myCookies.set('isAuth',false,{ path: '/' });
                this.setState({isLoading: false});
           }
    }

    render(){
        console.log('render app', this.state)
        if(this.state.isLoading){
            return <Loading/>;
        }
        return (
            <div>
                <BrowserRouter>
                    <div>
                    { this.myCookies.get('isAuth') === 'true' && <DrawerMenu onLogout={this.logout}/>}
                        <div className='page-content'>
                            <Routes/>
                        </div>
                    </div>
                </BrowserRouter>
            </div>
        );
    }
}

App.contextType = UserContext;

//export a component
export default withCookies(App);