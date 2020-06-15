// IMPORT LIB
import React, {Fragment} from 'react';
// CARD
import Card from '../bootstrap/Card/Card';
import CardBody from '../bootstrap/Card/CardBody';
import CardTitle from '../bootstrap/Card/CardTitle';
// BUTTON
import CardText from '../bootstrap/Card/CardText';
import ReceiptForm from '../form/ReceiptForm';
// IMPORT FUNCTION
import { capitalizeFirstLetter, takeTime } from '../../Utility/functions';


// CREATE A COMPONENT
const ReceiptsItem = ({day,fName,lName,className, id, matricola_stud, matricola_doc,onReceiptSubmit}) => {
    return (
        <Card className={className}>
            <CardBody>
                <CardTitle className='light-gray'>{capitalizeFirstLetter(fName)} {capitalizeFirstLetter(lName)}</CardTitle>
                <CardText className='receipt-date'>
                {
                   <Fragment>
                        <span>{day.slice(0,10)}</span>
                        <span className='receipt-time'>{takeTime(day)}</span>
                   </Fragment>
                }
                </CardText>
                <ReceiptForm 
                  matricola_studente={matricola_stud} 
                  matricola_docente={matricola_doc} 
                  date={day}
                  id={id}
                  onReceiptSubmit={onReceiptSubmit}
                  />
            </CardBody>
        </Card>
    )
}

// EXPORT A COMPONENT
export default ReceiptsItem;