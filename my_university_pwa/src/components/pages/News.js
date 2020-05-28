//import lib
import React, {Component} from 'react';
// LIST
import NewsList from '../list/NewsList';

//create a component 
class News extends Component {
    render(){
        return (
            <div>
                <NewsList/>
            </div>
        );
    }
}

//export a component 
export default News;