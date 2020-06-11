//iIMPORT LIB
import React, {Component} from 'react';
// CALENDAR
import CalendarView from '../calendar/CalendarView';
//API
import myUniversity from '../../API/myUniversity';
// FUNCTIONS
import {endTime,getLessonLocation} from '../../utility/functions';
// COOKIE
import {Cookies} from 'react-cookie';

//create a component 
class Calendar extends Component{
    constructor(props){
        super(props);

        this.cookies = new Cookies()

        this.state = {
            lessons: []
        }
    }

    getCalendar = (freshman) => {
        myUniversity.post('student/calendario', {matricola_studente: freshman})
                    .then(({data}) => {return data.map((lesson,index) => {
                        return (
                            {
                                title: lesson.titolo,
                                startDate: new Date(lesson.data_inizio),
                                endDate: endTime(lesson.data_inizio,lesson.numero_ore),
                                id: index,
                                location: getLessonLocation(lesson.nome_sede,lesson.numero_aula,lesson.numero_piano)
                            }
                        );
                    })})
                    .then(lessons => this.setState({lessons: lessons}))
                    .catch(error => console.log(`😱 Request failed: ${error}`));
    }

    componentDidMount(){
        const freshman = this.cookies.get('matricola_studente');
        this.getCalendar(freshman);
    }

    render(){
        console.log(this.state);
        return (
            <div>
                <div>Calendar page</div>
                <CalendarView/>
            </div>
        );
    }
}

//export a component 
export default Calendar;