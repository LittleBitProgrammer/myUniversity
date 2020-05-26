//import lib
import React, {Component} from 'react';
//BOOTSTRAP
import ResponsiveImage from '../bootstrap/ResponsiveImage';
//CARD
import Card from '../bootstrap/Card/Card';
import Row from '../bootstrap/Row';
import Column from '../bootstrap/Column';
import CardImage from '../bootstrap/Card/CardImage';
import CardBody from '../bootstrap/Card/CardBody';
import CardTitle from '../bootstrap/Card/CardTitle';
//iMAGE
import myUniversityLogo from '../../img/svg/graduation-hat-primary.svg'
import userLogo from '../../img/svg/user.svg'

//create a component 
class Login extends Component {
    constructor(props){
        super(props)

        this.state = {};
    }

    render(){
        return(
            <div>
                <div className='text-center'>
                    <ResponsiveImage path={myUniversityLogo} altText='Logo of My university'/>
                </div>
                <Card className='mt-3 border-primary border-2'>
                    <Row className='no-gutters'>
                        <Column sizeColumnClass='col-md-4'>
                            <CardImage path={userLogo} altText='User Logo' style={{width: '256px', padding: '5%'}}/>
                        </Column>
                        <Column sizeColumnClass='col-md-8'>
                            <CardBody>
                                <CardTitle className='text-primary'>Login</CardTitle>
                            </CardBody>
                        </Column>
                    </Row>
                </Card>
            </div>
        );
    }
}

//export a component 
export default Login;