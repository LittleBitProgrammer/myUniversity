//IMPORT LIB
import React, {Component} from 'react';
// ROUTER
import {BrowserRouter, Redirect} from 'react-router-dom';
//BOTTOMBAR
import BottomBar from './BottomBar';
//ROUTES
import Routes from './routes/Routes';
//COOKIE
import {Cookies, withCookies} from 'react-cookie';
import {instanceOf} from 'prop-types';
//API
import myUniversity from '../API/myUniversity';
// IMG
import Container from './bootstrap/Container';
import UserProvider from './context/UserProvider';

//TODO: UPDATE CONTEXT
//create a component 
class App extends Component {
    static propTypes = {
        cookies: instanceOf(Cookies).isRequired
      };

    constructor(props){
        super(props);

        this.myCookies = new Cookies()
        const {cookies} = props;

        this.state={
            matricola_studente: cookies.get('matricola_studente') || '',
            matricola_docente: cookies.get('matricola_docente') || '',
            password_studente: cookies.get('password_studente') || '',
            password_docente: cookies.get('password_docente') || '',
            isAuth: this.myCookies.get('isAuth') || false,
            userType: '',
            response: {}
        }
    }

    login = async() => {
        let response;
        let userType;
        //console.log('login',this.state.matricola_studente, this.state.password_studente)
        try{
            response = await myUniversity.post('/student/login', {
                matricola_studente: this.state.matricola_studente,
                password_studente: this.state.password_studente
            });
        }catch(error){
            console.log(`😱 There was an error: ${error}`);
            this.myCookies.set('isAuth',false,{ path: '/' });
        }
        if (response.data.length !== 0){
            this.myCookies.set('isAuth',true,{ path: '/' });
            userType = 'student';
        }else{
            try{
                response = await myUniversity.post('/professor/login',{
                    matricola_docente: this.state.matricola_docente,
                    password_docente: this.state.password_docente
                });
            }catch(error){
                console.log(`😱 There was an error: ${error}`);
                this.myCookies.set('isAuth',false,{ path: '/' });
            }

            if (response.data.length !== 0){
                this.myCookies.set('isAuth',true,{ path: '/' });
                userType = 'teacher';
            }else{
                this.myCookies.set('isAuth',false,{ path: '/' });
            }
        }

        this.setState({userType: userType, response:response.data[0]});
        console.log('home resp',this.state.response, 'home user type', this.state.userType);
    }

    componentDidMount(){
        console.log(this.state.matricola_studente,'-',this.state.password_studente,'-',this.state.matricola_docente,'-',this.state.password_docente);
        if((this.state.matricola_studente && this.state.password_studente) || 
           (this.state.matricola_docente && this.state.password_docente)){
               this.login();
           }else{
               this.setState({isAuth: false})
           }
    }

    render(){
        console.log('render cookie', this.myCookies.get('isAuth'));
        return (
            <div>
                <BrowserRouter>
                    <div>
                        { !this.state.isAuth && <Redirect to={{pathname: "/login"}}/>}
                        <Container>
                            <UserProvider>
                                <Routes userType={this.state.userType} response={this.state.response}/>
                            </UserProvider>
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
export default withCookies(App);