import React from "react";

class Events extends React.Component {
    constructor() {
        super();
        this.state = {
            value: '',
            isToggleOn: true,
            buttonValue: 'ON'
        }
    }

    showAlertBox = () => {
        alert("Hello world")
    }
    handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            alert(e.target.value)
        }

    }

    changeToggle = () => {
        if (this.state.isToggleOn) {
            this.setState({isToggleOn: false, buttonValue: "OFF"})
        } else {
            this.setState({isToggleOn: true, buttonValue: "ON"})
        }
    }


    render() {
        return (
            <div>
                {/*<input type="text" name="text"  onChange={this.handleKeyPress}/>*/}
                <input type="text" name="text" onKeyPress={this.handleKeyPress}/>
                <br/><br/>
                <button onClick={this.showAlertBox}>ClickMe</button>
                <br/><br/>
                <button onClick={this.changeToggle}>{this.state.buttonValue}</button>
            </div>)

    }
}

export default Events