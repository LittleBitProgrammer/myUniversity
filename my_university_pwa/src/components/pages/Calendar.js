//iIMPORT LIB
import React, {Component} from 'react';
// HEADER
import HeaderCalendar from '../wrapper/calendar/HeaderCalendar';
// CALENDAR
import CalendarView from '../calendar/CalendarView';
//MODAL
import Modal from '../modal/Modal';
import ModalHeader from '../modal/ModalHeader';
//API
import myUniversity from '../../API/myUniversity';
// FUNCTIONS
import {endTime,getSemester} from '../../Utility/functions';
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
            lessons: []
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
                        value: (
                        <React.Fragment>
                            <div className='discipline_name'>{appointment.nome_disciplina}</div>
                            <div>
                                <span className='floor-lesson'>{`Piano: ${appointment.numero_piano}`}</span>
                                <span className='room-lesson'>{`Aula: ${appointment.numero_aula}`}</span>
                            </div>
                            <div>{`Sede: ${appointment.nome_sede}`}</div>
                            <div className='teacher'>{`${appointment.nome} ${appointment.cognome}`}</div>
                        </React.Fragment>
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
    }

    onEventclick = (event) => {
        console.log(event.target)
        this.setState({
            isModalVisible: true,
        })
    }

    onEventClose = () => {
        this.setState({
            isModalVisible: false
        })
    }

    render(){
        console.log(this.state);
        return (
            <div>
                <HeaderCalendar 
                  year={this.year} 
                  courseName={this.state.lessons.length !== 0 ? this.state.lessons[0].nome_corso : 'Informatica'} 
                  semester={getSemester(new Date())}/>
                <CalendarView appointments={this.state.lessons} onEventClick={this.onEventclick}/>
                {this.state.isModalVisible && 
                <Modal className='modal' classContent='modal-content'>
                    <ModalHeader 
                      title='Gestici Avvisi' 
                      onCloseClick={this.onEventClose} 
                      color='white' textSize='h5' 
                      iconSize='h3'/>
                </Modal>
                }
            </div>
        );
    }
}



//export a component 
export default Calendar;