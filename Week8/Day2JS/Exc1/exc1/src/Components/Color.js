import React from "react";
import Phone from "./Phone";

class Color extends React.Component {
    constructor() {
        super();
        this.state = {
            favoriteColor: "Red"
        }
    }

    componentDidMount() {
        setTimeout( () => {
            this.setState({favoriteColor: "Blue"})
            console.log("hello")
        }, 3000)
    }

    render() {
        return (
            <div>
                <h1>My Favourite colour is {this.state.favoriteColor}</h1>
            </div>
        );
    }
}

export default Color
