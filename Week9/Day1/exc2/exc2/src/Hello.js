import App from "./App";
import {connect} from 'react-redux'
import React from "react";
import {changeTextFromRedux, handleChangeFromRedux, handleChangeFromReduxProp2} from "./actions";

const Hello = (props) => {
    return (
        <>
            <h3>Props from hello: {props.name}</h3>
            <h3>Props from hello connect : {props.prop_one}</h3>
            <h3>Text from Hello: {props.my_text}</h3>
            <button onClick={props.changeText}>Change Text from Redux to Property2</button>

        </>
    )
}
const mapStateToProps = (state) => {
    return {
        prop_one: state.property1,
        my_text: state.text
    }

}

const mapDispatchToProps = (dispatch) => {
    return {
        changeText: () => dispatch(changeTextFromRedux())
    }

}

export default connect(mapStateToProps, mapDispatchToProps)(Hello)