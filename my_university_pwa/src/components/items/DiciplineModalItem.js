//IMPORT LIB
import React, {Component,Fragment} from 'react';
//GRID
import Row from '../bootstrap/Row';
import Column from '../bootstrap/Column';
//BOOTSTRAP
import Switcher from '../bootstrap/Switcher';
//API
import myUniversity from '../../API/myUniversity';

//CREATE A COMPONENT
class DisciplineModalItem extends Component{
    constructor(props){
        super(props)

        this.state = {
            checked: this.props.isSubscribe
        }
    }

    postNewsletter = async(codice_corso,codice_disciplina,freshman) => {
        try{
            console.log('POST ', codice_corso,codice_disciplina,freshman)
            await myUniversity.post('/student/iscrizione_newsletter', {
                codice_corso: codice_corso,
                codice_disciplina: codice_disciplina,
                matricola_studente: freshman
            });
        }catch(error){
            console.log(`😱 Request failed: ${error}`);
        }
    }

    deleteNewsLetter = async(codice_corso,codice_disciplina,freshman) => {
        try{
            await myUniversity.post('/student/unfollow_newsletter', {
                codice_corso: codice_corso,
                codice_disciplina: codice_disciplina,
                matricola_studente: freshman
            });
        }catch(error){
            console.log(`😱 Request failed: ${error}`);
        }
    }

    onSwitchClick = (state) => {
        
        this.setState({
            checked: state
        });

        const {course_code,discipline_code,freshman} = this.props;

        if(state){
            // FROM FALSE TO TRUE
            this.postNewsletter(course_code,discipline_code,freshman);
        }else{
            // FROM TRUE TO FALSE
            this.deleteNewsLetter(course_code,discipline_code,freshman);
        }
    }


    render(){
        const {discipline_code,discipline_name,id,length} = this.props;
        return (
            <Fragment>
                <Row className='no-gutters p-4'>
                    <Column columnSize='8'>
                        {`${discipline_code} - ${discipline_name}`}
                    </Column>
                    <Column columnSize='4'>
                    
                        <Switcher 
                            className='float-right'
                            value={this.state.checked}
                            id={id} 
                            label={this.state.checked.toString()}
                            onClick={this.onSwitchClick}/>
                    </Column>
                </Row>
               { !(id === length) && <hr/>}
            </Fragment>
        );
    }
}

DisciplineModalItem.defaultProps = {
    discipline_code: 'error',
    discipline_name: 'error',
    isSubscribe: false,
}

// EXPORT A COMPONENT 
export default DisciplineModalItem;