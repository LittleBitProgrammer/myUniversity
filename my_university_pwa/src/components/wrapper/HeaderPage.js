// IMPORT LIB
import React from 'react';
// GRID UTILITY
import Row from '../bootstrap/Row';
import Column from '../bootstrap/Column';
//BOOTSTRAP
import Button from '../bootstrap/Button';

// CREATE A COMPONENT 
const HeaderPage = ({title,buttonTitle,buttonClick}) => {
    return (
        <Row className='justify-content-between light-gray no-gutters'>
            <Column columnSize='6'>
                <h3>{title}</h3>
            </Column>
            <Column columnSize='6'  className='justify-content-end'>
                <Button className='button-header' buttontext={buttonTitle} classColor='btn-primary' onClick={buttonClick}/>
            </Column>
        </Row>
    );
}

HeaderPage.defaultProps = {
    title: 'default',
    buttonTitle: 'default'
}

// EXPORT A COMPONENT 
export default HeaderPage;