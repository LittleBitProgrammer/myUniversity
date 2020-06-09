//import lib
import React, {Component} from 'react';
// API
import myUniversity from '../../API/myUniversity';
//COOKIE
import { Cookies } from 'react-cookie';
import ReceiptsList from '../list/ReceiptList';
// CSS
import '../../css/receipt.css';

//create a component 
class Receipts extends Component {
    constructor(props){
        super(props);

        this.myCookies = new Cookies();

        this.state = {
            allReceipts: [],
            receipts: []
        }
    }

    getReceipt = async () =>{
        try{
            const response = await myUniversity.post('/student/lista_prenotazioni_ricevimento',{
                                                    matricola_studente: this.myCookies.get('matricola_studente')});
            return response.data;

        }catch(error){
            console.log(`Request failed: ${error}`);
        }
    }

    getAllReceipt = async () =>{
        try{
            const response =  await myUniversity.post('/student/lista_ricevimenti_prenotabili',
                                                    {matricola_studente: this.myCookies.get('matricola_studente')});
            return response.data;
        }catch(error){
            console.log(`Request failed: ${error}`);
        }
    }

    async componentDidMount(){
        const AllReceipts = await this.getAllReceipt();
        const Receipts = await this.getReceipt();
        
        this.mergeReceipts(AllReceipts, Receipts);
    }

    mergeReceipts = (allReceipts, receipts) =>{
        let rewAllReceipts = [];

        if(allReceipts && receipts){
            allReceipts.forEach((allReceipt) => {
                let chk = false;

                receipts.forEach((receipt) =>{

                    var d1 = allReceipt.data_ricevimento;
                    var d2 = receipt.data_ricevimento;

                    var compare = d1.localeCompare(d2);
            
                    if(receipt.nome === allReceipt.nome && receipt.cognome === allReceipt.cognome && compare === 0){
                        chk = true
                    }
                });

                if(!chk){
                    rewAllReceipts.push({
                        cognome: allReceipt.cognome,
                        data_ricevimento: allReceipt.data_ricevimento,
                        email_docente: allReceipt.email_docente,
                        matricola_docente: allReceipt.matricola_docente,
                        nome: allReceipt.nome,
                        ore_ricevimento: allReceipt.ore_ricevimento
                    })
                };
            });

            this.setState({
                allReceipts: rewAllReceipts,
                receipts: receipts
            })
        }
        
    }

    render(){
        return(
            <div>
                <h3>Ricevimento</h3>
                <ReceiptsList allReceipts={this.state.allReceipts} mat={this.myCookies.get('matricola_studente')}/>
            </div>
        );
    }
}

//export a component
export default Receipts;