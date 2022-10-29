import React from "react";

class APIData extends React.Component {
    constructor() {
        super();
        this.state = {
            id: '',
            name: '',
            username: '',
            json: []
        }
    }

    async componentDidMount() {
        let response = await fetch(`https://jsonplaceholder.typicode.com/users`)
        // console.log("hi")
        let resp = await response.json()
        console.log(resp)
        this.setState({json: resp})

    }


    render() {
        const {id, name, username, json} = this.state;

        return (
            <div>
                <p>data {JSON.stringify(json)}</p>

                {json.map((item) => (
                    <div>{item.name}</div>
                ))}
            </div>


        )
    }

}

export default APIData