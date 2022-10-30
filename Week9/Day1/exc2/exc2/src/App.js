import logo from './logo.svg';
import {connect} from 'react-redux'
import './App.css';
import React from 'react';
import Hello from "./Hello";


class App extends React.Component {
    constructor() {
        super();
        this.state = {
            property1: "Prop1",
            property2: "Prop2"
        }
    }

    render() {
        return (
            <div>
                <h1>Redux Dude</h1>
                <h3>{this.state.property1}</h3>
                <h3>{this.state.property2}</h3>
                <h3>property from store: {this.props.prop_one}</h3>
                <Hello name={this.state.property1}/>
            </div>
        )
    }

}

const mapStateToProps = (state) => {//state from reducer
    return{
        prop_one:state.property1
    }

}
// const mapDispatchToProps = () => {
//
// }

// export default App
export default connect(mapStateToProps, null)(App);
