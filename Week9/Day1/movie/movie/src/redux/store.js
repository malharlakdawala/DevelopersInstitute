import {createStore} from "redux";
// import {reducer} from './reducers'
import {rootReducer} from "./reducers";


// const store = createStore(reducer)
const store = createStore(rootReducer)

export default store