// IMPORT LIB
import React, {Component} from 'react';
//WEEK-CALENDAR
import WeekCalendar from 'react-week-calendar';
//EVENT
import Event from './Event';
// MOMENT LIB
import moment from 'moment';
// FUNCTIONS
import {getMonday} from '../../Utility/functions';
// CSS
import '../../css/calendar.css';

// CREATE A COMPONENT
class CalendarView extends Component {

    render(){
        return(
            <WeekCalendar
              firstDay={getMonday(new Date())}
              numberOfDays={5}
              scaleUnit={30}
              startTime={moment({h: 9, m: 0})}
              endTime={moment({h: 18, m: 30})}
              dayFormat={'dddd DD'}
              eventSpacing={0}
              useModal={false}
              cellHeight={50}
              scaleHeaderTitle={moment().format('MMMM')}
              eventComponent={Event}
              selectedIntervals={this.props.appointments}
            />
        );
    }
}

// EXPORT A COMPONENT 
export default CalendarView;