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
//COOKIE
import {Cookies, withCookies} from 'react-cookie';
import {instanceOf} from 'prop-types';
//API
import myUniversity from '../API/myUniversity';
// IMG
import myUniversityLogo from '../img//svg//graduation-hat.svg';
import Container from './bootstrap/Container';

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
            isNavVisible:true
        }
    }

    login = async() => {
        let response;
        //console.log('login',this.state.matricola_studente, this.state.password_studente)
        try{
            response = await myUniversity.post('/student/login', {
                matricola_studente: this.state.matricola_studente,
                password_studente: this.state.password_studente
            });
        }catch(error){
            console.log(`😱 There was an error: ${error}`);
            this.myCookies.set('isLogged',false);
        }

        // console.log(response);

        if (response.data.length !== 0){
            this.setState({isNavVisible: true})
            this.myCookies.set('isLogged',true);
        }else{
            try{
                response = await myUniversity.post('/professor/login',{
                    matricola_docente: this.state.matricola_docente,
                    password_docente: this.state.password_docente
                });
            }catch(error){
                console.log(`😱 There was an error: ${error}`);
                this.myCookies.set('isLogged',false);
            }
        }

        if (response.data.length !== 0){
            this.setState({isNavVisible: true});
            this.myCookies.set('isLogged',true);
        }else{
            this.setState({isNavVisible: false})
            this.myCookies.set('isLogged',false);
        }
        //console.log(response)
    }

    componentDidMount(){
        console.log(this.state.matricola_studente,'-',this.state.password_studente,'-',this.state.matricola_docente,'-',this.state.password_docente);
        if((this.state.matricola_studente && this.state.password_studente) || 
           (this.state.matricola_docente && this.state.password_docente)){
               this.login();
           }else{
               this.setState({isNavVisible: false})
           }
    }

    render(){
        return (
            <div>
                <BrowserRouter>
                    <div>
                        { !this.state.isNavVisible && <Redirect to={{pathname: "/login"}}/>}
                        { this.state.isNavVisible && <Navigation 
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
                        </Navigation>}
                        <Container>
                            <Routes/>
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