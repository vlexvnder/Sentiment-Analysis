import React, { Component } from 'react';

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

    textAreaChange() {
        console.log(this.textArea.current.innerHTML)
    }

    render() { 
        return (
            <div ref={this.textArea} className="text-area" placeholder="Just start typing..." dangerouslySetInnerHTML={{__html: this.state.textAreaContent}} onInput={() => this.setState({ textAreaContent: this.textArea.current.innerHTML })} contentEditable></div>
        );
    }
}
 
export default TextArea;