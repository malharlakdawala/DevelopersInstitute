import {createStore} from "redux";
import {reducer} from "../reducers";

const store =createStore(reducer)
console.log("Store1", store.getState())


export default store