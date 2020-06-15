//iIMPORT LIB
import React, {Component} from 'react';
// HEADER
import HeaderCalendar from '../wrapper/calendar/HeaderCalendar';
// CALENDAR
import CalendarView from '../calendar/CalendarView';
//API
import myUniversity from '../../API/myUniversity';
// FUNCTIONS
import {endTime,getLessonLocation,getSemester} from '../../Utility/functions';
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
            lessons: []
        }
    }

    getCalendar = async(freshman) => {
        try{
            const response = await myUniversity.post('student/calendario', {matricola_studente: freshman});
            this.setState({lessons: response.data});
        }catch(error){
            console.log(`😱 Request failed: ${error}`);
        }
    }

    componentDidMount(){
        const freshman = this.cookies.get('matricola_studente');
        this.getCalendar(freshman);
    }

    render(){
        console.log(this.state);
        return (
            <div>
                <HeaderCalendar 
                  year={this.year} 
                  courseName={this.state.lessons.length !== 0 ? this.state.lessons[0].nome_corso : 'Informatica'} 
                  semester={getSemester(new Date())}/>
                <CalendarView/>
            </div>
        );
    }
}



//export a component 
export default Calendar;