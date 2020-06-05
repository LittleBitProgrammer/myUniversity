//import lib
import React, {Component} from 'react';
// API
import myUniversity from '../../API/myUniversity';
//COOKIE
import { Cookies } from 'react-cookie';
import ReceiptsList from '../list/ReceiptList';

//create a component 
class Receipts extends Component {
    constructor(props){
        super(props);

        this.myCookies = new Cookies();

        this.state = {
            receipts: [],
            isModalVisible: false
        }
    }

    getReceipt = async (freshman) =>{
        try{
            const response =  await myUniversity.post('/student/lista_ricevimenti_prenotabili',
                                                    {matricola_studente: freshman});
            this.setState({receipts: response.data});
        }catch(error){
            console.log(`Request failed: ${error}`);
        }
    }

    componentDidMount(){
        this.getReceipt(this.myCookies.get('matricola_studente'));
    }

    render(){
        return(
            <div>
                <h3 >Ricevimento</h3>
                <ReceiptsList receipts={this.state.receipts}/>
            </div>
        );
    }
}

//export a component
export default Receipts;