// IMPORT LIB
import React, {Component} from 'react';
// DRAWER COMPONENT
import Toggler from './drawer_components/Toggler';
import Header from './drawer_components/Header';
import Drawer from './drawer_components/Drawer';
import MenuList from './drawer_components/MenuList';
//NAV ITEM
import Navitem from '../../bootstrap/navigation/Navitem';
//COOKIE
import {Cookies} from 'react-cookie';
// SVG
import logo from '../../../img/svg/graduation-hat.svg';
import news from '../../../img/svg/news.svg';
import calendar from '../../../img/svg/calendar.svg';
import receipt from '../../../img/svg/receipt.svg';
import chat from '../../../img/svg/chat.svg';
import exit from '../../../img/svg/logout.svg';
import square from '../../../img/svg/square.svg';


//CREATE A COMPONENT
class DrawerMenu extends Component{
    constructor(props){
        super(props)

        this.myCookies = new Cookies();

        this.state = {
            isNavOpen: false
        }
    }

    toggleNav = () => {
        this.setState({
            isNavOpen: !this.state.isNavOpen
        });
    }

    //TODO ALT TEXT DYNAMIC IN NAVITEM
    //TODO LINK TO HOME ON MYUNIVERSITY CLICK
    render(){
        return(
            <React.Fragment>
                <Toggler onChange={this.toggleNav} checked={this.state.isNavOpen}/>
                <Header text='My university' logo={logo} altText='MyUniversity Logo' logoClass='logo'/>
                <Drawer>
                    <Navitem path='/profilo' onClick={this.toggleNav} liClass='drawer-profile' exact={true}>
                        <div className="img-container">
                            <img className="img-profile rounded" src={square} height="128" width="128" alt='profile img'/>
                            <h2>
                                {
                                 this.myCookies.get('userCookies').nome[0].toUpperCase() + 
                                 this.myCookies.get('userCookies').cognome[0].toUpperCase()
                                }
                            </h2>
                        </div>
                        <h6 className="freshman">Mat: {this.myCookies.get('userCookies').matricola_studente}</h6>
                    </Navitem>
                    <MenuList>
                        <Navitem path='/' name='News' logoImage={news} onClick={this.toggleNav} exact={true}/>
                        <Navitem path='/calendario' name='Calendario' onClick={this.toggleNav} logoImage={calendar}/>
                        <Navitem path='/ricevimento' name='Ricevimento' onClick={this.toggleNav} logoImage={receipt}/>
                        <Navitem path='/chat' name='Chat' onClick={this.toggleNav} logoImage={chat}/>
                    </MenuList>
                    <Navitem path='/login' name='Esci' logoImage={exit} liClass='exit' onClick={this.props.onLogout}/>
                </Drawer>
            </React.Fragment>
        );
    }
}

//EXPORT A COMPONENT
export default DrawerMenu;