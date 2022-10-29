import React from "react";

class Shop extends React.Component {
    constructor() {
        super();
        this.state = {
            hasError: true,
            error: '',
            errorInfo: ''
        }
    }

    componentDidCatch(error, errorInfo) {
        this.setState({
            error: error,
            errorInfo: errorInfo
        })
        console.log(this.state.error)
    }

    render() {
        if (this.state.hasError) {
            return (
                <div>
                    <p>Something went wrong... {this.state.hasError}</p><br></br>
                    <p><u>The error is</u> {this.state.error.toString()} </p><br></br>
                </div>

            )
        }
        // else{
        //     throw new Error("Error")
        // }
    }
}

export default Shop