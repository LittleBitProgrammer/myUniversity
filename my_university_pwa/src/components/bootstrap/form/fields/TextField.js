//import lib
import React, {Component} from 'react';

//create a component 
class TextField extends Component{

    composeTextField = () => {
        const {labelText,id,name,value,onChange,placeholder,required,className} = this.props;

        if(labelText){
            return(
                <div>
                    <label htmlFor={id}>{labelText}</label>
                    <input
                      className={`form-control ${className}`}
                      type='text'
                      id={id}
                      name={name}
                      value={value}
                      onChange={onChange}
                      placeholder={placeholder}
                      required={required}/>
                </div>
            );
        }else{
            return(
                <input
                  className={`form-control ${className}`}
                  type='text'
                  id={id}
                  name={name}
                  value={value}
                  onChange={onChange}
                  placeholder={placeholder}
                  required={required}/>
            );
        }
    }

    render(){
        return(
            this.composeTextField()
        );
    }
}

TextField.defaultProps = {
    className: 'mt-3'
}

//export a component 
export default TextField;