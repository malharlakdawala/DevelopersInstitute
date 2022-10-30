import React from "react";
import quotes from "./quotes";

// import tachyons;
class Showquotes extends React.Component {
    constructor() {
        super();
        this.state = {
            quote: '',
            author: '',
            colour: '',
            i: 0
        }
    }

    handleClick = () => {
        // console.log(quotes[0])
        this.setState({
            quote: quotes[this.state.i].quote,
            author: quotes[this.state.i].author,
            i: this.state.i + 1,
            colour: Math.random().toString(16).substr(-6)
        })
    }

    render() {
        const {quote, author,i, colour} = this.state
        return (
            <div style={{
                height: "80vh",
                width: "80vw",
                backgroundColor: "#" + colour,
                // display: "flex",
                justifyContent: "center",
                alignItems: "center",
            }}>
                <h1 >{quote}</h1> <br/> <br/>
                <h2>{this.state.author}</h2><br/> <br/>
                <button style={{backgroundColor: "#" + colour}} onClick={this.handleClick}>New Quote</button>

            </div>
        )
    }


}

export default Showquotes