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
import ModalBody from '../modal/ModalBody';
import DisciplineModalList from '../list/DisciplineModalList';
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
            discipline: [],
            newsletter:[],
            isModalVisible: false
        }
    }
    onNewsButtonClick = () => {
        this.setState({isModalVisible: true});
    }
    
    onModalButtonClick = () => {
        this.setState({isModalVisible: false});
    }

    //TODO BACKEND CONTROLLO SU DATA
    getAlert = async(freshman) => {
        try{
            const response = await myUniversity.post('/student/avvisi', 
                                               {matricola_studente: freshman});
            this.setState({news: response.data});
        }catch(error){
            console.log(`😱 Request failed: ${error}`);
        }
    }

    getDiscipline = async(freshman) => {
        try{
            const response = await myUniversity.post('/student/discipline_seguibili', {
                matricola_studente: freshman
            })
            this.setState({
                discipline: response.data
            });
        }catch(error){
            console.log(`😱 Request failed: ${error}`);
        }
    }

    getNewsLetter = async(freshman) => {
        try{
            const response = await myUniversity.post('/student/reperimento_lista_iscrizioni_newsletter', {
                matricola_studente: freshman
            });
            this.setState({
                newsletter: response.data
            });
        }catch(error){
            console.log(`😱 Request failed: ${error}`);
        }
    }

    async componentDidMount(){
        const freshman = this.myCookies.get('matricola_studente');
        await this.getAlert(freshman);
        await this.getDiscipline(freshman);
        await this.getNewsLetter(freshman);

        this.mergeNewsLetter(this.state.discipline, this.state.newsletter);
    }

    mergeNewsLetter = (discipline,newsletter) => {
        const rewrittenDiscipline = [];

        
        for(let i = 0; i < discipline.length ;i++){
            
            let chk = false;
            for(let j = 0; j < newsletter.length ;j++){
                if(discipline[i].codice_disciplina === newsletter[j].codice_disciplina){
                    chk = true;
                }
            }
            if(chk){
                rewrittenDiscipline.push({
                    anno: discipline[i].anno,
                    cfu: discipline[i].cfu,
                    codice_corso: discipline[i].codice_corso,
                    codice_disciplina: discipline[i].codice_disciplina,
                    nome_corso: discipline[i].nome_corso,
                    nome_disciplina: discipline[i].nome_disciplina,
                    semestre: discipline[i].semestre,
                    seguito: true
                });
            }else{
                rewrittenDiscipline.push({
                    anno: discipline[i].anno,
                    cfu: discipline[i].cfu,
                    codice_corso: discipline[i].codice_corso,
                    codice_disciplina: discipline[i].codice_disciplina,
                    nome_corso: discipline[i].nome_corso,
                    nome_disciplina: discipline[i].nome_disciplina,
                    semestre: discipline[i].semestre,
                    seguito: false
                });
            }
        }
        this.setState({
            discipline: rewrittenDiscipline
        });
    }

    render(){
        //console.log('NEWS', this.state)
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
                      <ModalBody>
                            <DisciplineModalList 
                              discipline={this.state.discipline} 
                              freshman={this.myCookies.get('matricola_studente')}/>
                      </ModalBody>
                </Modal>
                }
            </div>
        );
    }
}

//export a component 
export default News;