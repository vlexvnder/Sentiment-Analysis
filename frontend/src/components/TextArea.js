import React, { Component } from 'react';
import ContentEditable from 'react-contenteditable'

import './TextArea.css';

class TextArea extends Component {
    constructor(props) {
        super(props);

        this.state = { textAreaContent: '' };
        this.textArea = React.createRef();
    }

    componentDidMount() {
        this.textArea.current.focus();
    }

    contentEditableChange = event => {
        this.setState({ textAreaContent: event.target.value });
    }

    render() { 
        return (
            <ContentEditable className="text-area"
                innerRef={this.textArea}
                html={this.state.textAreaContent}
                disabled={false}
                onChange={this.contentEditableChange}
            />
        );
    }
}
 
export default TextArea;