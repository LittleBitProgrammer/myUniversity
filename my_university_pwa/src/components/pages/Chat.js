//import lib
import React, {Component} from 'react';

// WRAPPER
import SideChat from "../wrapper/Chat/SideChat";
import ChatVew from "../wrapper/Chat/ChatView";

// MODAL
import Modal from "../modal/Modal";
import ModalBody from "../modal/ModalBody";
import ModalHeader from "../modal/ModalHeader";

// GRID UTILITY
import Row from "../bootstrap/Row";
import Column from "../bootstrap/Column";

// API - MYUNIVERSITY
import myUniversity from "../../API/myUniversity";

// COOKIES
import {Cookies} from "react-cookie";

// CSS
import '../../css/modal.css';
import Button from "../bootstrap/Button";
import ChatModalList from "../list/ChatModalList";

//create a component
class Chat extends Component {

    constructor(props) {
        super(props);
        this.cookies = new Cookies();

        this.state = {
            isModalVisible : false,
            chats: [],
            contacts: []
        }
    }

    onButtonCLick=() => {
        this.setState({
            isModalVisible : true
        })
    }

    onModalClosed=() => {
        this.setState({
            isModalVisible : false
        })
    }

    async componentDidMount() {

        this.mergeChats();
    }
    
    getAllExistentChats = async() => {

        try {
            const response = await myUniversity.post('mongodb/get_all_conversations', {
                matricola: this.cookies.get('matricola_studente') });
                return response.data;

        }catch (error) {
            console.log(error);
        }

    }

    getAllContacts = async() => {
        try{
            const response = await myUniversity.post('/student/reperimento_lista_docenti_iscrizione_corso_piu_newsletter_per_chat', {
                matricola_studente: this.cookies.get('matricola_studente')});
            return response.data;

        }catch (error) {
            console.log(error)
        }
    }

    /*
    *     getAllExistentChats = () => {
        var chats = {chats: []};
        try {
            const response =  myUniversity.post('mongodb/get_all_conversations', {
                matricola: this.cookies.get('matricola_studente') }).then( (response) => {
                chats.chats = response.data;
            });
            return chats

        }catch (error) {
            console.log(error);
        }
    }

    getAllContacts = () => {
        var contacts = {contacts: []};
        try{
            const response =  myUniversity.post('/student/reperimento_lista_docenti_iscrizione_corso_piu_newsletter_per_chat', {
                matricola_studente: this.cookies.get('matricola_studente') }).then( (response) => {
                contacts.contacts = response.data;
            });
            return contacts;

        }catch (error) {
            console.log(error)
        }
    }
    * */

    mergeChats = () => {

        const chats = this.getAllExistentChats();
        const contacts = this.getAllContacts();



        console.log('chats',chats);
        console.log('contacts',contacts);
        let rewrittedChatList;
        let rewrittedContacts;

        chats.forEach((chat) => {
            contacts.forEach((contact) => {
                let chk = false;
                if(contacts.matricola_docente === chat.matricola1 || contacts.matricola_docente === chat.matricola2){
                    chk = true;
                }
                if(chk){
                    rewrittedChatList.push(
                        {
                            "id_conversation": chat.id_conversation,
                            "matricola_docente": contact.matricola_docente,
                            "nome_docente" : contact.nome,
                            "cognome_docente" : contact.cognome,
                            "matricola_studente": this.cookies.get("matricola_studente"),
                            "nome_studente" : this.cookies.get("nome"),
                            "cognome_studente" : this.cookies.get("cognome"),
                            "codice_disciplina" : chat.codice_disciplina,
                            "nome_disciplina" : chat.nome_disciplina,
                            "contacts": contact.contacts,
                            "messages": [
                                {
                                    "matricola_mittente": "string",
                                    "matricola_destinatario": "string",
                                    "messaggio": "string",
                                    "data_invio": "string"
                                }
                            ]
                        }
                    );
                }
            })
        })

        // abbiamo ordinato la lista dei nuovi contatti
        contacts.forEach((contact) => {
            chats.forEach((chat) => {
                let chk = false;
                if(contacts.matricola_docente === chat.matricola1 || contacts.matricola_docente === chat.matricola2){
                    chk = true;
                }
                if(chk === false){
                    rewrittedContacts.push(contact);

                }
            })
        })


        this.setState({
            chats: rewrittedChatList,
            contacts: rewrittedContacts
        })
    }

    render(){
        console.log('state', this.state)
        return (
            <div>
                <Row>
                    <Column columnSize='4'><SideChat onButtonCLick={this.onButtonCLick} chats={this.state.chats}/></Column>
                    <Column columnSize='8'><ChatVew/></Column>
                </Row>

                {this.state.isModalVisible &&
                <Modal className="modal" classContent="modal-content">
                    <ModalHeader title="Aggiungi chat" onCloseClick={this.onModalClosed} color="white" textSize="h5" iconSize="h3"/>
                    <ModalBody className="p-2">
                        <ChatModalList/>
                    </ModalBody>
                </Modal>}
            </div>
        );
    }
}


//export a component
export default Chat;


