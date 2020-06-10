// IMPORT LIB
import React from 'react';
import DisciplineModalItem from '../items/DiciplineModalItem';
import Container from '../bootstrap/Container';

// CREATE A COMPONENT
const DisciplineModalList = ({discipline,freshman}) => {
    //console.log('DISCIPLINE',discipline);
    
    const disciplineList = discipline.map((dis,index) => {
        //console.log('SINGOLO ELEMENTO', '-' , index, dis.seguito)
        return (<DisciplineModalItem 
                  key={index} 
                  id={index}
                  length={discipline.length-1}
                  discipline_name={dis.nome_disciplina} 
                  discipline_code={dis.codice_disciplina}
                  isSubscribe={dis.seguito}
                  freshman={freshman}
                  course_code={dis.codice_corso}
                  />
                );
    });

    return (
        <Container>{disciplineList}</Container>
    );
}

DisciplineModalList.defaultProps = {
    discipline:  []
}

// EXPORT A COMPONENT 
export default DisciplineModalList;