//import lib
import React, {Component} from 'react';

// WRAPPER
import SideChat from "../wrapper/Chat/SideChat/SideChat";
import ChatVew from "../wrapper/Chat/Body/ChatView";

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
import ChatModalList from "../list/ChatModalList";
import '../../css/chat.css';


//create a component
class Chat extends Component {

    constructor(props) {
        super(props);
        this.cookies = new Cookies();

        this.state = {
            isModalVisible : false,
            chats: [],
            contacts: [],
            chat_index: '',
            input_text: ''
        }
    }

    onSideChatItemClick = (index)=> {
        this.setState({
            chat_index: index
        })
    }

    onModalChatButtonCLick=() => {
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
        const chats = this.getAllExistentChats();
        const contacts = this.getAllContacts();


        chats.then( (response_chats) =>{
            contacts.then( (response_contacts) =>{
                this.mergeChats(response_chats, response_contacts);
            } )
        })
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

    mergeChats = (chats, contacts) => {

        let rewrittedChatList = [];
        let rewrittedContacts = [];

        if(chats && contacts){
            chats.forEach((chat) => {
                let chk = false;
                let tempContact;

                contacts.forEach((contact) => {
                    if(contact.matricola_docente === chat.matricola1 || contact.matricola_docente === chat.matricola2){
                        chk = true;
                        tempContact = contact;
                    }
                })

                if(chk){
                    rewrittedChatList.push(
                        {
                            id_conversation: chat.id_conversation,
                            matricola_docente: tempContact.matricola_docente,
                            nome_docente : tempContact.nome,
                            cognome_docente : tempContact.cognome,
                            matricola_studente: this.cookies.get("matricola_studente"),
                            nome_studente : this.cookies.get("userCookies").nome,
                            cognome_studente : this.cookies.get("userCookies").cognome,
                            codice_disciplina : tempContact.codice_disciplina,
                            nome_disciplina : tempContact.nome_disciplina,
                            contacts: tempContact.contatti,
                            messages: chat.messages
                        }
                    );
                }
            })

            // abbiamo ordinato la lista dei nuovi contatti
            contacts.forEach((contact) => {
                let chk = false;
                chats.forEach((chat) => {
                    if(contact.matricola_docente === chat.matricola1 || contact.matricola_docente === chat.matricola2){
                        chk = true;
                    }
                })
                if(chk === false){
                    rewrittedContacts.push(contact);
                }
            })

            this.setState({
                chats: rewrittedChatList,
                contacts: rewrittedContacts
            })
        }
    }

    onModalItemCLick = async (matricola_docente)=> {
        //TODO RITORNA INDICE DI CONVERSAZIONE, UTILIZZARE PER IMPOSTARE IL FOCUS SULLA CONVERSAZIONE
        let respose = await myUniversity.post("/mongodb/create_new_conversation", {
            matricola1: this.cookies.get("matricola_studente"),
            matricola2: matricola_docente
        });
        this.onModalClosed();
        const chat = await this.getAllExistentChats();
        const cont = await this.getAllContacts();
        this.mergeChats(chat,cont);
        this.setState({
            chat_index: respose.data.id_conversation
        })
    }

    onInputChange = (inputText) => {
        this.setState({
            input_text: inputText
        })
    }

    onMessageSend = async() => {
        let matricola_docente = this.state.chats[this.state.chats.findIndex((obj)=>obj.id_conversation === this.state.chat_index)].matricola_docente;
        console.log('matricola_docente - send message', matricola_docente);
        try {
            await myUniversity.post('/mongodb/send_message', {
                id_conversation: this.state.chat_index,
                matricola_mittente: this.cookies.get('matricola_studente'),
                matricola_destinatario: matricola_docente,
                messaggio: this.state.input_text
            });

        }catch (error) {
            console.log(error);
        }

    }

    // CANCELLARE IL TESTO NEL MESSAGETEXT ALL'iNVIO DEL MESSAGGIO
    render(){
        console.log(this.state)
        return (
            <div>
                <Row>
                    <Column columnSize='5'>
                        <SideChat onButtonClick={this.onModalChatButtonCLick}
                                  onItemClick={this.onSideChatItemClick}
                                  chats={this.state.chats}/>
                    </Column>
                    <Column columnSize='7'>
                        <ChatVew
                            chats={this.state.chats}
                            chat_index={this.state.chat_index}
                            onInputChange={this.onInputChange}
                            onMessageSend={this.onMessageSend}/>
                    </Column>
                </Row>
                {this.state.isModalVisible &&
                <Modal className="modal" classContent="modal-content">
                    <ModalHeader title="Aggiungi chat" onCloseClick={this.onModalClosed} color="white" textSize="h5" iconSize="h3"/>
                    <ModalBody className="p-2">
                        <ChatModalList contacts={this.state.contacts} onModalItemCLick={this.onModalItemCLick}/>
                    </ModalBody>
                </Modal>}
            </div>
        );
    }
}

//export a component
export default Chat;

