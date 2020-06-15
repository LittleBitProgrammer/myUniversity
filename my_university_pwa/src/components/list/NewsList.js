// IMPORT LIB
import React from 'react';
// ITEM
import AlertItem from '../wrapper/AlertItem';

// TODO:// CARD COLOR

// CREATE A COMPONENT
const NewsList = ({news}) => {

    const newsList = news.map((item,index) => {
        return (
            <AlertItem 
              key={index}
              id={index}
              className='mt-3 news-card'
              title={item.titolo_avviso}
              discipline={item.nome_disciplina}
              fName={item.nome}
              lName={item.cognome}
              body={item.corpo_avviso}/>
        );
    });

    return <div className='mt-3'>{newsList}</div>;
}

// EXPORT A COMPONENT 
export default NewsList;