import logo from './logo.svg';
import React from "react";
import './App.css';
import Firstname from "./components/firstname";
import Secondname from "./components/secondname";
import ClickButton from "./components/clickButton";
import ShowResult from "./components/results";

class App extends React.Component {
    constructor(props) {
        super();
        this.state = {
            firstname: "",
            secondname: "",
            results:{}
        }
    }

    handleChange = (e) => {
        this.setState({[e.target.name]: e.target.value})
    }

    buttonClicked = () => {
        console.log("buttonclicked")
        const options = {
            method: 'GET',
            headers: {
                'X-RapidAPI-Key': 'd6a2e73179mshfa5a8a3fa183d90p1a1499jsn14c184f39007',
                'X-RapidAPI-Host': 'love-calculator.p.rapidapi.com'
            }
        };

        fetch(`https://love-calculator.p.rapidapi.com/getPercentage?sname=${this.state.firstname}&fname=${this.state.secondname}`, options)
            .then(response => response.json())
            .then(response => {
                console.log()
                this.setState({results:response})
            })
            .catch(err => console.error(err));

    }

    render() {
        // console.log(this.state.firstname, this.state.secondname)
        console.log(this.state.results)

        return (
            <div className="App-header">

                <>
                    <Firstname handleChange={this.handleChange}/>
                    <Secondname handleChange={this.handleChange}/><br/>
                    <ClickButton buttonClicked={this.buttonClicked}/>
                    <ShowResult result={this.state.results}/>
                </>
            </div>
        )
    }

}

export default App;
