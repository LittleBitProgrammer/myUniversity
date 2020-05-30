// IMPORT LIB
import React, {Component} from 'react';
// CARD COMPONENT
import Card from '../bootstrap/Card/Card';
import CardBody from '../bootstrap/Card/CardBody';
import CardTitle from '../bootstrap/Card/CardTitle';
// GRID COMPONENT
import Row from '../bootstrap/Row';
import Column from '../bootstrap/Column';
//UTILITY
import RoundImage from '../bootstrap/RoundImage';

//TODO: dynamic alt text

// CREATE A COMPONENT
class ProfileInformation extends Component {
    // CLASS CONSTRUCTOR
    constructor(props){
        super(props)

        this.state = {
            // insert information here
        }
    }

    //RENDER METHOD
    render(){
        return(
          <Card className='border-0'>
            <Row className='no-gutters'>
                <Column screnSize='md' columnSize='4' className='card-wrapper'>
                    <RoundImage 
                      path='https://www.lascimmiapensa.com/wp-content/uploads/2019/03/Al-Bano-1.jpg' 
                      altText='immagine di "NOME" "COGNOME"' 
                      className='mx-auto d-block p-3'
                      roundClass='custom-circle-image'
                      />
                </Column>
                <Column screnSize='md' columnSize='8'>
                    <CardBody>
                        <CardTitle>Profilo</CardTitle>
                    </CardBody>
                </Column>
            </Row>
          </Card>  
        );
    }
}

// EXPORT A COMPONENT
export default ProfileInformation;