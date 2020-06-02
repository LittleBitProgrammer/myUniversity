// IMPORT LIB
import React from 'react';
import Column from '../Column';
import Row from '../Row';

// CREATE A COMPONENT
const TabRow = ({classNAme,title,attribute}) => {
    return (
        <Row className={classNAme}>
            <Column columnSize='6'>
                <label>{title}</label>
            </Column>
            <Column columnSize='6'>
                <p>{attribute}</p>
            </Column>
        </Row>
    );
}

TabRow.defaultProps = {
    title: '',
    attribute: ''
}

// EXPORT A COMPONENT
export default TabRow;