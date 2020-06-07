//import lib
import React, {Component} from 'react';
// LIST
import NewsList from '../list/NewsList';
// API
import myUniversity from '../../API/myUniversity';
// COOKIE
import {Cookies} from 'react-cookie';
// WRAPPER
import HeaderPage from '../wrapper/HeaderPage';
//MODAL
import Modal from '../modal/Modal';
import ModalHeader from '../modal/ModalHeader';
// CSS
import '../../css/news.css';
import '../../css/modal.css';



//create a component 
class News extends Component {
    constructor(props){
        super(props);

        this.myCookies = new Cookies();

        this.state = {
            news: [],
            isModalVisible: false
        }
    }
    onNewsButtonClick = () => {
        this.setState({isModalVisible: true});
    }
    
    onModalButtonClick = () => {
        this.setState({isModalVisible: false});
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
        return (
            <div>
                <HeaderPage title='Avvisi' buttonTitle='Gestisci Newsletter' buttonClick={this.onNewsButtonClick}/>
                <NewsList news={this.state.news}/>
                {this.state.isModalVisible && 
                <Modal className='modal' classContent='modal-content'>
                    <ModalHeader 
                      title='Gestici Avvisi' 
                      onCloseClick={this.onModalButtonClick} 
                      color='white' textSize='h5' 
                      iconSize='h3'/>
                </Modal>
                }
            </div>
        );
    }
}

//export a component 
export default News;