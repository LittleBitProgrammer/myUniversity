// IMPORT LIB
import React, {Component} from 'react';

//CREATE A COMPONENT
class DrawerMenu extends Component{
    constructor(props){
        super(props)

        this.state = {
            isNavOpen: false
        }
    }
    render(){
        return(
            <div>Hello world</div>
        );
    }
}

//EXPORT A COMPONENT
export default DrawerMenu;