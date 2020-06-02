// IMPORT LIB
import React from 'react';
import Column from '../Column';
import Row from '../Row';

// CREATE A COMPONENT
const TabRow = ({title,attribute}) => {
    return (
        <Row>
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