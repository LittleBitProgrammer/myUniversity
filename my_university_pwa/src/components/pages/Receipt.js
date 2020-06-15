//import lib
import React, {Component} from 'react';
// API
import myUniversity from '../../API/myUniversity';
//COOKIE
import { Cookies } from 'react-cookie';
import ReceiptsList from '../list/ReceiptList';
// FUNCTIONS
import {remove} from '../../Utility/functions';
// CSS
import '../../css/receipt.css';

//create a component 
class Receipts extends Component {
    constructor(props){
        super(props);

        this.myCookies = new Cookies();

        this.state = {
            allPossibleReceipts: []
        }
    }

    onReceiptSubmit = (matricola_docente,date,matricola_studente,inputText,id) => {
        try{
            myUniversity.post('/student/richiesta_ricevimento', {
                            'matricola_docente': matricola_docente,
                            'data_ricevimento': date,
                            'matricola_studente': matricola_studente,
                            'motivazione_ricevimento': inputText})
        }catch(error){
            console.log(`There was an error: ${error}`);
        }
        const newPossibleReceipt = remove(id,this.state.allPossibleReceipts);
        this.setState({allPossibleReceipts: newPossibleReceipt});
    }

    getReceipt = async (freshman) =>{
        try{
            const response = await myUniversity.post('/student/lista_prenotazioni_ricevimento',{
                                                    matricola_studente: freshman});
            return response.data;

        }catch(error){
            console.log(`Request failed: ${error}`);
        }
    }

    getAllPossibleReceipt = async (freshman) =>{
        try{
            const response =  await myUniversity.post('/student/lista_ricevimenti_prenotabili',
                                                    {matricola_studente: freshman});
            return response.data;
        }catch(error){
            console.log(`Request failed: ${error}`);
        }
    }

    async componentDidMount(){
        const freshman = this.myCookies.get('matricola_studente');

        const AllPossibleReceipts = await this.getAllPossibleReceipt(freshman);
        const Receipts = await this.getReceipt(freshman);
        
        this.mergeReceipts(AllPossibleReceipts, Receipts);
    }

    mergeReceipts = (allPossibleReceipts, receipts) =>{
        let rewAllPossibleReceipts = [];

        if(allPossibleReceipts.length !== 0 && receipts.length !== 0){
            allPossibleReceipts.forEach((allReceipt) => {
                let chk = false;

                receipts.forEach((receipt) =>{

                    let d1 = allReceipt.data_ricevimento;
                    let d2 = receipt.data_ricevimento;

                    let compare = d1.localeCompare(d2);
            
                    if(receipt.nome === allReceipt.nome && receipt.cognome === allReceipt.cognome && compare === 0){
                        chk = true
                    }
                });

                if(!chk){
                    rewAllPossibleReceipts.push({
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
                allPossibleReceipts: rewAllPossibleReceipts
            })
        }else{
            this.setState({
                allPossibleReceipts: allPossibleReceipts
            });
        }
        
    }

    render(){
        return(
            <div className='pb-4'>
                <h3 className='light-gray'>Ricevimento</h3>
                <ReceiptsList 
                  allPossibleReceipts={this.state.allPossibleReceipts} 
                  mat={this.myCookies.get('matricola_studente')}
                  onReceiptSubmit={this.onReceiptSubmit}
                  />
            </div>
        );
    }
}

//export a component
export default Receipts;