// IMPORT LIB
import React from 'react';
// ITEM 
import ReceiptsItem from '../items/ReceiptsItem';

// CREATE A COMPONENT
const ReceiptsList = ({allReceipts, mat}) => {
    const receiptsList = allReceipts.map((item, index) =>{
        return(
            <ReceiptsItem
                key={index}
                id={index}
                day={item.data_ricevimento}
                fName={item.nome}
                lName={item.cognome}
                className='mt-3 border-primary'
                matricola_stud={mat}
                matricola_doc={item.matricola_docente}

            />
        );
    });

    return <div className='mt-3'>{receiptsList}</div>
}

// EXPORT A COMPONENT
export default ReceiptsList