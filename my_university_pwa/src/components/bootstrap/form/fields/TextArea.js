import TextareaAutosize from 'react-textarea-autosize';
import React, {Component} from "react";

class TextArea extends Component {

    onChange = async(event)=>{
        event.preventDefault();
        if(this.props.textCallback){
            this.props.textCallback(event.target.value);
        }
        console.log(event.target);
    }

    render() {
        return(<TextareaAutosize
            id={this.props.id}
            maxRows={this.props.maxRows}
            minRows={this.props.minRows}
            value={this.props.inputValue}
            className={this.props.className?this.props.className: ''}
            onChange={this.onChange}
            placeholder={this.props.placeholder}

        />)
    }
}

export default TextArea;

