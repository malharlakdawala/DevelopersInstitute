// import logo from './logo.svg';
import './App.css';
import './style.css';
import Users from './Users.json';
// import Hello from "./Hello";
import User from "./User";
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

function App() {
    console.log(Users);

    return (
        <div>
            <h1>Hello</h1>

            {
                Users.map(item => {
                        return (
                            <User key={item.id} name={item.name} username={item.username} email={item.email}/>
                        )
                    }
                )
            }


        </div>
    )

}

export default App;