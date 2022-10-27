import React from "react";

class Events extends React.Component {
    constructor() {
        super();
        this.state={
            value:''
        }
    }

    showAlertBox = () => {
        alert("Hello world")
    }
    handleKeyPress=(e)=>{
        if(e.key==='Enter'){
            alert(e.target.value)
        }

    }


    render() {
        return (
            <div>
                {/*<input type="text" name="text"  onChange={this.handleKeyPress}/>*/}
                <input type="text" name="text" onKeyPress={this.handleKeyPress} />
                <br/><br/>
                <button onClick={this.showAlertBox}>ClickMe</button>
            </div>)

    }
}

export default Events