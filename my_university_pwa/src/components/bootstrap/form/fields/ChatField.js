import TextareaAutosize from 'react-textarea-autosize';
import React, {Component} from "react";

class ChatField extends Component {
    onChange = (event)=>{
        this.props.textCallback(event.target.value);
    }

    render() {
        return(<TextareaAutosize
            maxRows={this.props.maxRows}
            value={this.props.value}
            className={this.props.className?this.props.className: ''}
            onChange={this.onChange}
            placeholder={this.props.placeholder}

        />)
    }

}

export default ChatField;

