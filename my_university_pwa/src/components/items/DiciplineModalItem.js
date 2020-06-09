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

        //console.log('LOG PROPS SWITCH',props);

        this.state = {
            checked: this.props.isSubscribe
        }
    }

    postNewsletter = async(codice_corso,codice_disciplina,matricola_studente,data_iscrizione) => {
        try{
            await myUniversity.post('/student/iscrizione_newsletter', {
                codice_corso: codice_corso,
                codice_disciplina: codice_disciplina,
                matricola: matricola_studente,
                data_iscrizione: data_iscrizione
            });
        }catch(error){
            console.log(`😱 Request failed: ${error}`);
        }
    }

    onSwitchClick = () => {
        this.setState({
            checked: !this.state.checked
        });

        console.log('state - switch', this.state.checked)
    }


    render(){
        //console.log('from item', this.state.checked)
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
                            id={`switcher${id}`} 
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