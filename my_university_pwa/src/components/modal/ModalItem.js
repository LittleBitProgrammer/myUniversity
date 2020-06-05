// IMPORT LIB
import React from 'react';

// CREATE A COMPONENT
const ModalItem = ({onClick, disciplineCode, disciplineName, teacherSName, teacherName, matricolaDocente})=>{
    return (
        <div className="pointer pt-3 pb-3" onClick={() => { onClick(matricolaDocente) }}>
            <p className="h6"> {`${disciplineCode} - ${disciplineName} - ${teacherSName}  ${teacherName}`}</p>
        </div>
    )
}

// EXPORT A COMPONENT
export default ModalItem;