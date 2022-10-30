import logo from './logo.svg';
import './App.css';
import Lesson from './Lesson';
import React from 'react';
import {createStore} from "redux";
import reducer from "./reducers";
import Day from './Day';
import {store} from "./store";


class App extends React.Component {
    constructor() {
        super();
    }

    render() {
        return (
            <div>
                <Day weekday={store.getState().weekday}/>
            </div>
        )
    }

}

export default App;
