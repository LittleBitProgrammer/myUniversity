//iIMPORT LIB
import React, {Component} from 'react';
// HEADER
import HeaderCalendar from '../wrapper/calendar/HeaderCalendar';
// CALENDAR
import CalendarView from '../calendar/CalendarView';
//MODAL
import Modal from '../modal/Modal';
import ModalHeader from '../modal/ModalHeader';
import ModalBody from '../modal/ModalBody';
//GRID
import Row from '../bootstrap/Row';
import Column from '../bootstrap/Column';
//API
import myUniversity from '../../API/myUniversity';
// FUNCTIONS
import {endTime,endMinutes,getSemester} from '../../Utility/functions';
// MOMENT LIB
import moment from 'moment';
// COOKIE
import {Cookies} from 'react-cookie';

//create a component 
class Calendar extends Component{
    constructor(props){
        super(props);

        this.cookies = new Cookies()
        this.year = moment().format('YYYY');

        this.state = {
            isModalVisible: false,
            indexSelected: 0,
            lessons: [],
            receipts: []
        }
    }

    getReceipt = async(freshman) => {
        try{
            const response =  await myUniversity.post('/student/lista_prenotazioni_ricevimento',{
                matricola_studente: freshman
            })
            console.log('RESPONSE', response);
            const mappedResponse = response.data.map((receipt) => {
                console.log('DATA RIC', moment(receipt.data_ricevimento) )
                return (
                    {
                        uid: receipt.matricola_docente + receipt.data_ricevimento,
                        start: receipt.ora_inizio ? moment(receipt.ora_inizio) : moment(receipt.data_ricevimento),
                        end: receipt.ora_inizio ? endMinutes(receipt.ora_inizio,receipt.durata) :  endMinutes(receipt.data_ricevimento,30)
                    }
                );
            });
            this.setState({receipts: mappedResponse});
        }catch(error){
            console.log(`😱 Request failed: ${error}`);
        }
    }
 
    getCalendar = async(freshman) => {
        try{
            const response = await myUniversity.post('student/calendario', {matricola_studente: freshman});
            const mapped_response = response.data.map((appointment,index) => {
                return (
                    {
                        uid: index,
                        start: moment(appointment.data_inizio),
                        end: endTime(appointment.data_inizio,appointment.numero_ore),
                        title: appointment.titolo,
                        discipline: appointment.nome_disciplina,
                        floor_number: appointment.numero_piano,
                        room_number: appointment.numero_aula,
                        headOffice: appointment.nome_sede,
                        teacher: `${appointment.nome} ${appointment.cognome}`,
                        description: appointment.descrizione,
                        value: (
                        <div onClick={(event) => {this.onEventclick(event)}} id={index} className='calendar-custom-content'>
                            <div className='discipline_name'>{appointment.nome_disciplina}</div>
                            <div>
                                <span className='floor-lesson'>{`Piano: ${appointment.numero_piano}`}</span>
                                <span className='room-lesson'>{`Aula: ${appointment.numero_aula}`}</span>
                            </div>
                            <div>{`Sede: ${appointment.nome_sede}`}</div>
                            <div className='teacher'>{`${appointment.nome} ${appointment.cognome}`}</div>
                        </div>
                        )
                    }
                );
            });

            this.setState({lessons: mapped_response});
        }catch(error){
            console.log(`😱 Request failed: ${error}`);
        }
    }

    componentDidMount(){
        const freshman = this.cookies.get('matricola_studente');
        this.getCalendar(freshman);
        this.getReceipt(freshman);
    }

    onEventclick = (event) => {
        event.stopPropagation();
        console.log('ID',event.target.parentNode.id)
        console.log('LESSONS', this.state.lessons);
        this.setState({
            isModalVisible: true,
            indexSelected: event.target.parentNode.id ? event.target.parentNode.id : event.target.id
        })
    }

    onEventClose = () => {
        this.setState({
            isModalVisible: false
        })
    }

    render(){
        console.log('STATE', this.state);
        const selectedAppointment = this.state.lessons[this.state.indexSelected];
        return (
            <div>
                <HeaderCalendar 
                  year={this.year} 
                  courseName={this.state.lessons.length !== 0 ? this.state.lessons[0].nome_corso : 'Informatica'} 
                  semester={getSemester(new Date())}/>
                <CalendarView appointments={this.state.lessons.concat(this.state.receipts)}/>
                {this.state.isModalVisible && 
                <Modal className='modal' classContent='modal-content-little'>
                    <ModalHeader 
                      title={selectedAppointment.title}
                      onCloseClick={this.onEventClose} 
                      color='white' textSize='h5' 
                      iconSize='h3'/>
                    <ModalBody>
                        {/*TODO:// ADD CONDITIONAL RENDERING FOR RECEIPT*/}
                        <Row>
                            <Column className='left-key' columnSize='5'>Disciplina:</Column>
                            <Column className='right-key' columnSize='7'>{selectedAppointment.discipline}</Column>
                        </Row>
                        <Row>
                            <Column className='left-key' screenSize='lg' columnSize='5'>Piano:</Column>
                            <Column className='right-key' screenSize='lg' columnSize='7'>{selectedAppointment.floor_number}</Column>
                        </Row>
                        <Row>
                            <Column className='left-key' screenSize='lg' columnSize='5'>Aula:</Column>
                            <Column className='right-key' screenSize='lg' columnSize='7'>{selectedAppointment.room_number}</Column>
                        </Row>
                        <Row>
                            <Column className='left-key' columnSize='5'>Sede:</Column>
                            <Column className='right-key' columnSize='7'>{selectedAppointment.headOffice}</Column>
                        </Row>
                        <Row>
                            <Column className='left-key' columnSize='5'>Professore:</Column>
                            <Column className='right-key' columnSize='7'>{selectedAppointment.teacher}</Column>
                        </Row>
                        <hr/>
                        <Row className='pb-4'>
                            <Column className='left-key' columnSize='12'>Descrizione</Column>
                            <Column className='right-key description' columnSize='12'>{selectedAppointment.description}</Column>
                        </Row>
                    </ModalBody>
                </Modal>
                }
            </div>
        );
    }
}



//export a component 
export default Calendar;