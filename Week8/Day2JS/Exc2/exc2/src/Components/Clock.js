import React from "react";

class Clock extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            currentTime: Date()
        }
    }
    //
    // tick = () => {
    //     this.setState({currentTime: Date().toLocaleString()})
    //     console.log("asdfsda")
    // }

    componentDidMount() {
        setInterval(() => {
            this.setState({currentTime: Date()})
        }, 1000)
    }

    render() {
        return (
            <div>
                <h1>hello World</h1>
                <h2>{this.state.currentTime}</h2>

            </div>
        );
    }

}


export default Clock
