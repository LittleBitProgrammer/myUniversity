//import lib
import React, {Component} from 'react';
// LIST
import NewsList from '../list/NewsList';
// API
import myUniversity from '../../API/myUniversity';
// COOKIE
import {Cookies} from 'react-cookie';
// WRAPPER
import NewsHeader from '../wrapper/HeaderPage';
// CSS
import '../../css/news.css';

//create a component 
class News extends Component {
    constructor(props){
        super(props);

        this.myCookies = new Cookies();

        this.state = {
            news: []
        }
    }

    getAlert = async(freshman) => {
        try{
            const response = await myUniversity.post('/student/avvisi', 
                                               {matricola_studente: freshman});
            this.setState({news: response.data});
        }catch(error){
            console.log(`😱 Request failed: ${error}`);
        }

    }
    componentDidMount(){
        this.getAlert(this.myCookies.get('matricola_studente'));
    }

    render(){
        console.log(this.state.news);
        return (
            <div>
                <NewsHeader title='Avvisi' buttonTitle='Gestisci Newsletter'/>
                <NewsList news={this.state.news}/>
            </div>
        );
    }
}

//export a component 
export default News;