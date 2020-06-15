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
            indexSelected: '',
            lessons: [],
            receipts: [],
            colors:[]
        }
    }

    getColors = async() => {
        try{
            const response = await myUniversity.post('/mongodb/get_all_colors');
            this.setState({
                colors: response.data
            });
        }catch(error){
            console.log(`😱 Request failed: ${error}`);
        }
    }

    getReceipt = async(freshman) => {
        try{
            const response =  await myUniversity.post('/student/lista_prenotazioni_ricevimento',{
                matricola_studente: freshman
            })
            const mappedResponse = response.data.map((receipt) => {
                return (
                    {
                        uid: receipt.matricola_docente + receipt.data_ricevimento,
                        start: receipt.ora_inizio ? moment(receipt.ora_inizio) : moment(receipt.data_ricevimento),
                        end: receipt.ora_inizio ? endMinutes(receipt.ora_inizio,receipt.durata) :  endMinutes(receipt.data_ricevimento,30),
                        title: `Ricevimento Prof. ${receipt.nome} ${receipt.cognome}`,
                        email: receipt.email_docente,
                        freshman: receipt.matricola_docente,
                        startHour: moment(receipt.ora_inizio),
                        duration: receipt.durata,
                        value: (
                            <div 
                              onClick={(event) => {this.onEventclick(event)}} 
                              id={receipt.matricola_docente + receipt.data_ricevimento} 
                              className='calendar-custom-content'>
                                <div className='discipline_name'>{`Ricevimento Prof: ${receipt.nome} ${receipt.cognome}`}</div>
                            </div>
                        )
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
                        uid: index.toString(),
                        start: moment(appointment.data_inizio),
                        end: endTime(appointment.data_inizio,appointment.numero_ore),
                        color: '#fff',
                        title: appointment.titolo,
                        discipline: appointment.nome_disciplina,
                        floor_number: appointment.numero_piano,
                        room_number: appointment.numero_aula,
                        headOffice: appointment.nome_sede,
                        teacher: `${appointment.nome} ${appointment.cognome}`,
                        description: appointment.descrizione,
                        courseCode: appointment.codice_corso,
                        disciplineCode: appointment.codice_disciplina,
                        value: (
                        <div onClick={(event) => {this.onEventclick(event)}} id={index} className='calendar-custom-content'>
                            <div className='discipline_name'>{appointment.nome_disciplina}</div>
                            <React.Fragment>
                                <span className='floor-lesson'>{`Piano: ${appointment.numero_piano}`}</span>
                                <span className='room-lesson'>{`Aula: ${appointment.numero_aula}`}</span>
                            </React.Fragment>
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

    mergeCalendar = (lessons,colors) => {
        const rewrittenLessons = this.state.lessons;

        
        for(let i = 0; i < lessons.length ;i++){
            
            let chk = false;
            let temp;
            for(let j = 0; j < colors.length ;j++){
                if(rewrittenLessons[i].courseCode === colors[j].codice_corso && rewrittenLessons[i].disciplineCode === colors[j].codice_disciplina){
                    chk = true;
                    temp = colors[j]
                }
            }
            if(chk){
                rewrittenLessons[i].color = temp.colore_esadecimale;
            }
        }

        this.setState({
            lessons: rewrittenLessons
        })
    }

    async componentDidMount(){
        const freshman = this.cookies.get('matricola_studente');
        await this.getCalendar(freshman);
        this.getReceipt(freshman);
        await this.getColors();
        this.mergeCalendar(this.state.lessons,this.state.colors);

    }

    onEventclick = (event) => {
        event.stopPropagation();
        this.setState({
            isModalVisible: true,
            indexSelected: event.target.parentNode.id ? (event.target.parentNode.id).toString() : event.target.id.toString()
        })
    }

    onEventClose = () => {
        this.setState({
            isModalVisible: false
        })
    }

    render(){
        const concat = this.state.lessons.concat(this.state.receipts)
        const selectedAppointment = concat[concat.findIndex((obj)=>obj.uid === this.state.indexSelected)];
        return (
            <div>
                <HeaderCalendar 
                  year={this.year} 
                  courseName={this.state.lessons.length !== 0 ? this.state.lessons[0].nome_corso : 'Informatica'} 
                  semester={getSemester(new Date())}/>
                <CalendarView appointments={concat}/>
                {this.state.isModalVisible && 
                <Modal className='modal' classContent='modal-content-little'>
                {( selectedAppointment.uid.length <= 10) &&
                    <React.Fragment>
                    <ModalHeader 
                      title={selectedAppointment.title}
                      onCloseClick={this.onEventClose} 
                      color='white' textSize='h5' 
                      iconSize='h3'/>
                    <ModalBody>
                        <Row>
                            <Column className='left-key' columnSize='5'>Disciplina:</Column>
                            <Column className='right-key' columnSize='7'>{selectedAppointment.discipline}</Column>
                        </Row>
                        <Row>
                            <Column className='left-key' columnSize='5'>Piano:</Column>
                            <Column className='right-key' columnSize='7'>{selectedAppointment.floor_number}</Column>
                        </Row>
                        <Row>
                            <Column className='left-key' columnSize='5'>Aula:</Column>
                            <Column className='right-key' columnSize='7'>{selectedAppointment.room_number}</Column>
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
                </React.Fragment>
                }
                {!(selectedAppointment.uid.length <= 10) &&
                    <React.Fragment>
                        <ModalHeader 
                        title={selectedAppointment.title}
                        onCloseClick={this.onEventClose} 
                        color='white' textSize='h5' 
                        iconSize='h3'/>
                        <ModalBody>
                            <Row>
                                <Column className='left-key' columnSize='12'>Informazioni Professore</Column>
                            </Row>
                            <Row className='mt-3'>
                                <Column className='left-key' columnSize='5'>Email:</Column>
                                <Column className='right-key' columnSize='7'>{selectedAppointment.email}</Column>
                            </Row>
                            <Row className='mt-2'>
                                <Column className='left-key' columnSize='5'>Matricola Docente:</Column>
                                <Column className='right-key' columnSize='7'>{selectedAppointment.freshman}</Column>
                            </Row>
                            <hr/>
                                <Row className='mt-2'>
                                    <Column className='left-key' columnSize='12'>Informazioni Ricevimento</Column>
                                </Row>
                                <Row className='mt-3'>
                                    <Column className='left-key' columnSize='5'>Ora inizio:</Column>
                                    <Column className='right-key' columnSize='7'>{selectedAppointment.startHour.format('HH:mm')}</Column>
                                </Row>
                                <Row className='mt-2 pb-4'>
                                    <Column className='left-key' columnSize='5'>Durata:</Column>
                                    <Column className='right-key' columnSize='7'>{selectedAppointment.duration}</Column>
                                </Row>
                        </ModalBody>
                    </React.Fragment>
                }
                </Modal>
                }
            </div>
        );
    }
}



//export a component 
export default Calendar;