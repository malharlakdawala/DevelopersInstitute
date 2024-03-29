// import logo from './logo.svg';
import React from 'react';
import './App.css';
import './style.css';
import SearchBox from "./components/SearchBox";
import {Button} from "react-bootstrap";
// import Users from './Users.json';
// import Hello from "./Hello";
import User from "./components/User";
import 'tachyons';
// import Hello from "./Hello";

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }
//
// export default App;
// function App() {
//     const users =[
//         {name: "Malhar", username:"malharlakdwala", email:"malharldawala@gmail.com"},
//         {name: "David", username:"davidlakdwala", email:"david@gmail.com"},
//         {name: "Lucas", username:"lucaslasdf", email:"lucas@gmail.com"}
//     ]
//
//     return (
//         <div className="App">
//             <header className="App-header">
//                 Hello folks Malhar here
//                 <Hello/>
//                 {
//                     users.map((item,i)=>{
//                         return(
//                             <User name={item.name} username={item.username} email={item.email}/>
//                         )
//                     })
//                 }
//                 {/*<User name={"Malhar"} username={"malharlakdawala"} email={"malharlakdawala@gmail.com"}/>*/}
//                 {/*<User name={"Chotu"} username={"chotuachahe"} email={"masthe@fasd.com"}/>*/}
//             </header>
//         </div>
//     );
// }
//
// export default App;

class App extends React.Component {
    constructor() {
        super();
        this.state = {
            txt: "",
            arr: [1, 3, 4],
            users: [],
            input_search_text:""
        }
        console.log("constructor")
    }

    componentDidMount() {
        fetch('https://jsonplaceholder.typicode.com/users')
            .then(res => res.json())
            .then(data => {
                // console.log(data)
                this.setState({users: data})
            })
            .catch(err => {
                console.log("Error", err)
            })
        console.log("componentDidMount")
    }

    handleChange = (e) => {
        console.log(e.target.value)
        this.setState({txt: e.target.value})
    }
    handleClick=()=>{
        this.setState({input_search_text: this.state.txt})
    }

    handleUsers = () => {
        fetch('https://jsonplaceholder.typicode.com/users')
            .then(res => res.json())
            .then(data => {
                // console.log(data)
                this.setState({users: data})
            })
            .catch(err => {
                console.log("Error", err)
            })

    }

    render() {
        const {users, txt,input_search_text} = this.state;
        const filterusers = users.filter(item => {
            return item.name.toLowerCase().includes(input_search_text.toLowerCase());
        })
        console.log("text ", txt)
        console.log("render")
        console.log(this.state.arr)
        return (
            <div>
                <h1>Users {this.state.txt}</h1>
                <SearchBox searchFunction={this.handleChange} clickFunction={this.handleClick}/>
                <Button onClick={this.handleUsers}>Get Users</Button>
                {
                    filterusers.map(item => {
                        return (
                            // <User key={item.id} name={item.name} username={item.username} email={item.email}/>
                            <User key={item.id} user={item}/>
                        )
                    })}
            </div>
        )
    }

}

export default App;

// function App() {
//     console.log(Users);
//
//     return (
//         <div>
//             <h1>Hello</h1>
//
//             {
//                 Users.map(item => {
//                         return (
//                             // <User key={item.id} name={item.name} username={item.username} email={item.email}/>
//                             <User key={item.id} user={item}/>
//                         )
//                     }
//                 )
//             }
//
//
//         </div>
//     )
//
// }
//
// export default App;