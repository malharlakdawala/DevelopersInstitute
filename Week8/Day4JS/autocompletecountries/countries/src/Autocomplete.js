import React from "react";
import countries from "./countries";

class Autocomplete extends React.Component {
    constructor() {
        super();
        this.state = {
            suggestions: [],
            text: ''
        }
    }

    handleClick = () => {
        // console.log(countries)

    }
    handleChange = (e) => {
        const inputkey = e.target.value
        let matchingCountries = countries.filter(name => name.toLowerCase().indexOf(inputkey) > -1)
        if ((1 < matchingCountries.length && matchingCountries.length<150)) {
            this.setState({suggestions: matchingCountries})
        }
        if(e.target.value===''){
            this.setState({suggestions: []})
        }
    }

    render() {
        const {suggestions, text} = this.state;

        return (
            <div>
                <h1>Autocomplete Country Names</h1>
                <form>
                    Country Name: <input type="text" name="countryname" onClick={this.handleClick}
                                         onChange={this.handleChange}/><br/>

                    {suggestions.map((item) => (
                        <div>{item}</div>
                    ))}
                    Number of suggestions: {suggestions.length}

                </form>

            </div>
        )


    }

}

export default Autocomplete