import {connect} from 'react-redux'
import React from "react";
import './App.css';
import {addCounter, subtractCounter, filterContentFromStatements} from './actions/index'

class App extends React.Component {
    constructor() {
        super();
        this.state = {
            count: 4
        }

    }


    render() {
        console.log(this.props.statementsArray)
        return (
            <div style={{"text-align": "center"}}>
                <h1>Redux Dude</h1>
                <h3>{this.props.count}</h3>
                <button onClick={this.props.addCount}>Add</button>
                <button onClick={this.props.subtractCount}>Subtract</button><br/><br/>
                <input type="text" onKeyPress={this.props.filterContent}/>
                {this.props.statementsArray.map((item) => (
                    <div><a href={item.url}>{item.title}</a></div>
                ))}


            </div>
        )
    }

}

const mapStateToProps = (state) => {
    return {
        // count: state.countervalue
        statementsArray: state.inputStatements
    }
}
const mapDispatchToProps = (dispatch) => {
    return {
        addCount: () => dispatch(addCounter()),
        subtractCount: () => dispatch(subtractCounter()),
        filterContent: (e)=> dispatch(filterContentFromStatements(e.target.value))

    }
}
export default connect(mapStateToProps, mapDispatchToProps)(App);
