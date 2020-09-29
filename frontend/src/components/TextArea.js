import React, { Component } from 'react';

import './TextArea.css';

class TextArea extends Component {
    constructor(props) {
        super(props);

        this.textArea = React.createRef();
    }

    componentDidMount() {
        this.textArea.current.focus();
    }

    render() { 
        return (
            <div ref={this.textArea} className="text-area" placeholder="Just start typing..." contentEditable>
                
            </div>
        );
    }
}
 
export default TextArea;