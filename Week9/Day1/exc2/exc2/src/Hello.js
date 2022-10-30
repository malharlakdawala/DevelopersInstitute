import App from "./App";
import {connect} from 'react-redux'

const Hello = (props) => {
    return (
        <>
            <h3>Props from hello: {props.name}</h3>
            <h3>Props from hello connect : {props.prop_one}</h3>
        </>
    )
}
const mapStateToProps = (state) => {
    return {
        prop_one: state.property1
    }

}
export default connect(mapStateToProps, null)(Hello)