//import lib
import React, {Component} from 'react';

//create a component 
class Receipt extends Component {
    constructor(props){
        super(props)

        this.state = {
            // insert props here
        }
    }

    componentDidMount(){
        // insert axios call here
    }

    render(){
        return(
            <div>Receipt Component :)</div>
        );
    }
}

//export a component
export default Receipt;