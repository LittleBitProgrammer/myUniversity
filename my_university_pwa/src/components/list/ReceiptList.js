// IMPORT LIB
import React from 'react';
// ITEM 
import ReceiptsItem from '../wrapper/ReceiptsItem';

// CREATE A COMPONENT
const ReceiptsList = ({receipts, mat}) => {
    const receiptsList = receipts.map((item, index) =>{
        return(
            <ReceiptsItem
                key={index}
                id={index}
                day={item.data_ricevimento}
                fName={item.nome}
                lName={item.cognome}
                className='mt-3 border-primary'
                matricola={mat}
            />
        );
    });

    return <div className='mt-3'>{receiptsList}</div>
}

// EXPORT A COMPONENT
export default ReceiptsList