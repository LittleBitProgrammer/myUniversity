//import lib
import React, {Component} from 'react';
// LIST
import NewsList from '../list/NewsList';
//CONTEXT
import {UserContext} from '../context/UserContext';

//create a component 
class News extends Component {

    render(){
        let matricola = this.context;
        return (
            <div>
                {console.log('prova',matricola)}
                <NewsList/>
            </div>
        );
    }
}
News.contextType = UserContext;

//export a component 
export default News;