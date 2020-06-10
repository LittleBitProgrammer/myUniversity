//IMPORT LIB
import React, {Component} from 'react';

//CREATE A COMPONENT 
class Switcher extends Component{
    constructor(props){
        super(props)

        this.state = {
            checked: this.props.value
        }
    }

    switchValue = () => {
        this.props.onClick(!this.state.checked,this.props.id);
        this.setState({checked: !this.state.checked});
    }

    render(){
        const {className,id,label} = this.props;
        return (
            <div className={`custom-control custom-switch pointer${className ? ' ' + className : ''}`}>
                <input 
                    type='checkbox'
                    className='custom-control-input pointer'
                    id={id}
                    checked={this.state.checked}
                    onChange={this.switchValue}
                    />
                    <label className="custom-control-label" htmlFor={id}>{label? label : ''}</label>
            </div>
        );
    }
}

Switcher.defaultProps = {
    value: false,
    id: 'defaultChecked',
    className: '',
    label: ''
}

//EXPORT A COMPONENT 
export default Switcher;