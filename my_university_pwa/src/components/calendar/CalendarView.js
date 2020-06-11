// IMPORT LIB
import React, {Component} from 'react';
//WEEK-CALENDAR
import WeekCalendar from 'react-week-calendar';
const moment = require('moment');

// CREATE A COMPONENT
class CalendarView extends Component {
    constructor(props){
        super(props)

        // CAMBIARE QUI PER IMPOSTARE IL PRIMO GIORNO
        this.momentObj = new moment("2020-06-12", moment.ISO_8601);
    }
    render(){
        return(
            <WeekCalendar
              firstDay={this.momentObj}
              numberOfDays={7}
            />
        );
    }
}

// EXPORT A COMPONENT 
export default CalendarView;