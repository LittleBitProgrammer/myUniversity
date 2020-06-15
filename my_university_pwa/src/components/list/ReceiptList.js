// IMPORT LIB
import React from 'react';
// ITEM 
import ReceiptsItem from '../items/ReceiptsItem';
// IMPORT FUNCTION
import { takeDate, takeTime } from '../../utility/functions';

// CREATE A COMPONENT
const ReceiptsList = ({allPossibleReceipts, mat,onReceiptSubmit}) => {
    const receiptsList = allPossibleReceipts.map((item, index) =>{
        return(
            <ReceiptsItem
                key={item.matricola_docente + takeDate(item.data_ricevimento) + takeTime(item.data_ricevimento)}
                id={index}
                day={item.data_ricevimento}
                fName={item.nome}
                lName={item.cognome}
                className='mt-3 border-primary'
                matricola_stud={mat}
                matricola_doc={item.matricola_docente}
                onReceiptSubmit={onReceiptSubmit}
            />
        );
    });
    return <div className='mt-3'>{receiptsList}</div>
}

// EXPORT A COMPONENT
export default ReceiptsList