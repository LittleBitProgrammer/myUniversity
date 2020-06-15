// IMPORT LIB
import React, {Component} from 'react';
// CARD
import Card from '../bootstrap/Card/Card';
import CardBody from '../bootstrap/Card/CardBody';
import CardTitle from '../bootstrap/Card/CardTitle';
import CardText from '../bootstrap/Card/CardText';
// FUNCTIONS
import {capitalizeFirstLetter} from '../../Utility/functions';

// CREATE A COMPONENT
class AlertItem extends Component {

    render(){
        const { id,title,discipline,fName,lName,body,className } = this.props;
        return (
            <a 
              className='news'
              data-toggle='collapse' 
              role='button'
              href={`#collapseAlert${id}`}
              aria-expanded='false' 
              aria-controls={`collapseAlert${id}`}>
                <Card className={className}>
                    <CardBody>
                        <CardTitle>{capitalizeFirstLetter(title)}</CardTitle>
                        
                            <CardText>
                                {`${discipline} - Prof. ${capitalizeFirstLetter(fName)} ${capitalizeFirstLetter(lName)}`}
                            </CardText>
                        <div className='collapse' id={`collapseAlert${id}`}>
                            <CardText>
                                {body}
                            </CardText>
                        </div>
                    </CardBody>
                </Card>
            </a>);   
    }
}

// EXPORT A COMPONENT
export default AlertItem;