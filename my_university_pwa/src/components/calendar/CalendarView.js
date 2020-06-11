// IMPORT LIB
import React, {Component} from 'react';
//WEEK-CALENDAR
import WeekCalendar from 'react-week-calendar';
// MOMENT LIB
import moment from 'moment';
// FUNCTIONS
import {getMonday} from '../../utility/functions';

// CREATE A COMPONENT
class CalendarView extends Component {
    constructor(props){
        super(props)

        // CAMBIARE QUI PER IMPOSTARE IL PRIMO GIORNO
        //console.log(this.momentObj = new moment("2020-06-12", moment.ISO_8601));
    }
    render(){
        return(
            <WeekCalendar
              firstDay={getMonday(new Date())}
              numberOfDays={7}
            />
        );
    }
}

// EXPORT A COMPONENT 
export default CalendarView;