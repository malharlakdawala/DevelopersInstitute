import React from "react";

class Phone extends React.Component {
    constructor() {
        super();
        this.state = {
            brand: "Samsung",
            model: "Galaxy S20",
            color: "black",
            year: 2020
        }
    }
    changeColour=()=>{

        this.setState({color: "red"})
    }

    render(){
        return(
            <div>
                <h1>hello Phone</h1>
                <p>Brand: {this.state.brand}</p>
                <p>Model: {this.state.model}</p>
                <p>Color: {this.state.color}</p>
                <p>Year: {this.state.year}</p>
                <button onClick={this.changeColour}>Change Colour</button>
            </div>
        )
    }
}


export default Phone
