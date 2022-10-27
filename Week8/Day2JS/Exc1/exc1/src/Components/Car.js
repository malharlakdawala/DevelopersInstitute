import React from 'react'
import Garage from './Garage'

class CarDetails extends React.Component {
    constructor(props) {
        super(props);
        this.state = {'color': 'red'}
    }

    render() {
        const {modelName} = this.props;
        return (

            <div>
                <h1>This is {modelName} of colour {this.state.color}</h1>
                <p>asdf</p>
                <Garage size={"Small"}/>
            </div>)
    }
}

export default CarDetails