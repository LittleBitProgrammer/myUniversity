// IMPORT LIB
import React from 'react';
// CARD
import Card from '../bootstrap/Card/Card';
import CardBody from '../bootstrap/Card/CardBody';
import CardTitle from '../bootstrap/Card/CardTitle';
// BUTTON
import CardText from '../bootstrap/Card/CardText';
import ReceiptForm from '../form/ReceiptForm';
// IMPORT FUNCTION
import { capitalizeFirstLetter } from '../../utility/functions';


// CREATE A COMPONENT
const ReceiptsItem = ({day,fName,lName,className, id, matricola_stud, matricola_doc}) => {

    return (
        <Card className={className}>
            <CardBody>
                <CardTitle>{capitalizeFirstLetter(fName)} {capitalizeFirstLetter(lName)}</CardTitle>
                <CardText>{`${day}`}</CardText>
                <ReceiptForm matricola_studente={matricola_stud} matricola_docente={matricola_doc} date={day}/>
            </CardBody>
        </Card>
    )
}

// EXPORT A COMPONENT
export default ReceiptsItem;