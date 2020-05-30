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
//CONTEXT
import {UserContext} from '../context/UserContext';
//FUNCTIONS
import {capitalizeFirstLetter} from '../../Utility/functions';
//IMAGES
import squareLogo from '../../img/svg/square-1.svg'

//TODO: dynamic alt text
//TODO: fix image size on smaller screen
//TODO: teacher content
//TODO: dynamic background image

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
        const user = this.context;
        console.log(user);
        return(
            <div>
                <p className='h4'> Profilo</p>
                <Card className='mt-5'>
                    <Row className='align-items-center'>
                    <Column screnSize='sm' columnSize='2'>
                        {/* Lasciare vuoto*/}
                    </Column>
                    <Column  screnSize='sm' columnSize='1.5'>
                        <RoundImage 
                          path={squareLogo}
                          altText='immagine di "NOME" "COGNOME"' 
                          roundClass='profile-circle-image'
                          className='circle-border-primary'
                        />
                    </Column>
                    <Column screnSize='sm' columnSize='2'>
                        {/* Lasciare vuoto*/}
                        ciao mondo
                    </Column>
                    <Column screnSize='sm' columnSize='2'>
                        {/* Lasciare vuoto*/}
                        ciao mondo
                    </Column>
                    <Column screnSize='sm' columnSize='4'>
                        {/* Lasciare vuoto*/}
                        ciao mondo
                    </Column>
                    </Row>
                    <Row className=' align-items-center'>
                        <Column screnSize='md' columnSize='8'>
                            <CardBody>
                                <p className='h2 text-primary'>{`${capitalizeFirstLetter(user.student.nome)} 
                                                                ${capitalizeFirstLetter(user.student.cognome)}`}</p>
                                <p>Mat: {user.student.matricola_studente}</p>
                            </CardBody>
                        </Column>
                    </Row>
                </Card> 
            </div> 
        );
    }
}

//DEFINE CONTEXT OF THE CLASS
ProfileInformation.contextType = UserContext;

// EXPORT A COMPONENT
export default ProfileInformation;