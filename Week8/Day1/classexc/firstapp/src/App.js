import Hello from "./Hello";
import User from "./User"
import './App.css';

function App() {
    const users =[
        {name: "Malhar", username:"malharlakdwala", email:"malharldawala@gmail.com"},
        {name: "David", username:"davidlakdwala", email:"david@gmail.com"},
        {name: "Lucas", username:"lucaslasdf", email:"lucas@gmail.com"}
    ]

    return (
        <div className="App">
            <header className="App-header">
                Hello folks Malhar here
                <Hello/>
                {
                    users.map((item,i)=>{
                        return(
                            <User name={item.name} username={item.username} email={item.email}/>
                        )
                    })
                }
                {/*<User name={"Malhar"} username={"malharlakdawala"} email={"malharlakdawala@gmail.com"}/>*/}
                {/*<User name={"Chotu"} username={"chotuachahe"} email={"masthe@fasd.com"}/>*/}
            </header>
        </div>
    );
}

export default App;
