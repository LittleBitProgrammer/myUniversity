// IMPORT LIB
import React, {Component} from 'react';
//NAV ITEM
import Navitem from '../../bootstrap/navigation/Navitem';
//COOKIES
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
                <input 
                  type="checkbox" 
                  id="drawer-toggle" 
                  name="drawer-toggle" 
                  onChange={this.toggleNav} 
                  checked={this.state.isNavOpen}/>
                <label htmlFor="drawer-toggle" id="drawer-toggle-label"></label>
                <header>
                    My university
                    <img src={logo} alt='MyUniversity Logo' className='logo'/>
                </header>
                <nav id="drawer">
                    <div className="img-container">
                        <img className="img-profile rounded" src={square} height="128" width="128" alt='profile img'/>
                        <h2>RV</h2>
                    </div>
                    <h6 className="freshman">Mat: 0124001871</h6>
                    <ul>
                        <Navitem path='/' name='News' logoImage={news} onClick={this.toggleNav} exact={true}/>
                        <Navitem path='/calendario' name='Calendario' onClick={this.toggleNav} logoImage={calendar}/>
                        <Navitem path='/ricevimento' name='Ricevimento' onClick={this.toggleNav} logoImage={receipt}/>
                        <Navitem path='/chat' name='Chat' onClick={this.toggleNav} logoImage={chat}/>
                    </ul>
                    <Navitem path='/login' name='Esci' logoImage={exit} liClass='exit' onClick={this.props.onLogout}/>
                </nav>
            </React.Fragment>
        );
    }
}

//EXPORT A COMPONENT
export default DrawerMenu;