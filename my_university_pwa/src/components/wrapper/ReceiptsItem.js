// IMPORT LIB
import React, {Component} from 'react';
// CARD
import Card from '../bootstrap/Card/Card';
import CardBody from '../bootstrap/Card/CardBody';
import CardTitle from '../bootstrap/Card/CardTitle';
// TEXT
import TextField from '../bootstrap/form/fields/TextField';
// FUNCTIONS
import {capitalizeFirstLetter} from '../../utility/functions';
// BUTTON
import Button from '../bootstrap/Button';
import Column from '../bootstrap/Column';
import CardText from '../bootstrap/Card/CardText';

// CREATE A COMPONENT
class ReceiptsItem extends Component {

    render(){
        const {day,fName,lName,className} = this.props;
        return (
            <Card className={className}>
                <CardBody>
                    <CardTitle>{capitalizeFirstLetter(fName)} {capitalizeFirstLetter(lName)}</CardTitle>
                    <CardText>{`${day}`}</CardText>
                    <form>
                        <div >
                            <TextField placeholder='Matricola, Es. 0124001910'></TextField>
                            <input type='text' className='form-control form-control-lg mt-3' placeholder='Motivazione, Es."Spiegazione generatore di grafi"'></input>
                            <Column columnSize='6' className='justify-content-end'>
                                <Button className='btn btn-primary mt-1 button-header' buttontext='Invia'></Button>
                            </Column>
                        </div>
                    </form>
                </CardBody>
            </Card>
        )
    }
}

// EXPORT A COMPONENT
export default ReceiptsItem;