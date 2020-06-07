// IMPORT LIB
import React from 'react';
// CARD
import Card from '../bootstrap/Card/Card';
import CardBody from '../bootstrap/Card/CardBody';
import CardTitle from '../bootstrap/Card/CardTitle';
// FUNCTIONS
import {capitalizeFirstLetter} from '../../utility/functions';
// BUTTON
import CardText from '../bootstrap/Card/CardText';
import ReceiptForm from '../form/ReceiptForm';


// CREATE A COMPONENT
const ReceiptsItem = ({day,fName,lName,className, id, matricola}) => {

    return (
        <a 
            className='news'
            data-toggle='collapse' 
            role='button'
            href={`#collapseReceipt${id}`}
            aria-expanded='false' 
            aria-controls={`collapseReceipt${id}`}>

            <Card className={className}>
                <CardBody>
                    <CardTitle>{capitalizeFirstLetter(fName)} {capitalizeFirstLetter(lName)}</CardTitle>
                    <CardText>{`${day}`}</CardText>
                    <div className='collapse' id={`collapseReceipt${id}`}>
                        <ReceiptForm matricola_studente={matricola}/>
                    </div>
                </CardBody>
            </Card>
        </a>
    )
}

// EXPORT A COMPONENT
export default ReceiptsItem;