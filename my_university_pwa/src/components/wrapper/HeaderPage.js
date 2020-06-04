// IMPORT LIB
import React from 'react';
// GRID UTILITY
import Row from '../bootstrap/Row';
import Column from '../bootstrap/Column';
//BOOTSTRAP
import Button from '../bootstrap/Button';

// CREATE A COMPONENT 
const NewsHeader = ({title,buttonTitle}) => {
    return (
        <Row className='justify-content-between'>
            <Column columnSize='6'>
                <h3>{title}</h3>
            </Column>
            <Column columnSize='6'  className='justify-content-end'>
                <Button className='button-header' buttontext={buttonTitle} classColor='btn-primary'/>
            </Column>
        </Row>
    );
}

NewsHeader.defaultProps = {
    title: 'default',
    buttonTitle: 'default'
}

// EXPORT A COMPONENT 
export default NewsHeader;