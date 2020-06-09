import TextareaAutosize from 'react-textarea-autosize';
import React, {Component} from "react";

class TextArea extends Component {

    constructor(props) {
        super(props);
        this.state = {
            inputValue: ''
        }
    }

    onChange = (event)=>{
        event.preventDefault();
        this.setState({
            inputValue: event.target.value
        });
        if(this.props.textCallback){
            this.props.textCallback(this.state.inputValue);
        }
    }



    render() {
        return(<TextareaAutosize
            maxRows={this.props.maxRows}
            value={this.state.inputValue}
            className={this.props.className?this.props.className: ''}
            onChange={this.onChange}
            placeholder={this.props.placeholder}

        />)
    }

}

export default TextArea;

