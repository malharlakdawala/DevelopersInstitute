import React from "react";

class Garage extends React.Component {
    render() {
        const {size} = this.props;
        return <h2>The garage size is {size}</h2>
    }
}
export default Garage