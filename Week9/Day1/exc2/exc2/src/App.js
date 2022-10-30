import logo from './logo.svg';
import {connect} from 'react-redux'
import './App.css';
import React from 'react';
import Hello from "./Hello";
import {handleChangeFromRedux, handleChangeFromReduxProp2, changeTextFromRedux} from "./actions";


class App extends React.Component {
    constructor() {
        super();
        this.state = {
            property1: "Prop1",
            property2: "Prop2"
        }
    }

    handleChanegAppState = (e) => {
        this.setState({property1: e.target.value})
    }

    render() {
        return (
            <div>
                <h1>Redux Dude</h1>
                <h3>{this.state.property1}</h3>
                <h3>{this.state.property2}</h3>
                <h3>property from store: {this.props.prop_one}</h3>
                <input type="text" onChange={this.handleChanegAppState}/>
                <input type="text" onChange={this.props.myHandleChange}/>
                <Hello name={this.state.property1}/>
                <br/>
                <h3>Property2 from Redux: {this.props.prop_two}</h3>
                <input type="text" onChange={this.props.myHandleChangeProp2}/>
                <br/>
                <h4>Text from redux: {this.props.text_from_redux}</h4>

            </div>
        )
    }

}

const mapStateToProps = (state) => {//state from reducer
    return {
        prop_one: state.property1,
        prop_two: state.property2,
        text_from_redux:state.text
    }

}
const mapDispatchToProps = (dispatch) => {
    return {
        myHandleChange: (e) => dispatch(handleChangeFromRedux(e.target.value)),
        myHandleChangeProp2: (e) => dispatch(handleChangeFromReduxProp2(e.target.value)),
        changeText: (e) => dispatch(changeTextFromRedux("hello"))
    }

}

// export default App
export default connect(mapStateToProps, mapDispatchToProps)(App);
