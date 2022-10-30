import logo from './logo.svg';
import './App.css';
import Autocomplete from "./Autocomplete";
import Showquotes from "./showquotes";
import Todo from "./todo"

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/*<Autocomplete/> /!* uncomment this to get autocomplete country code*!/*/}
        {/*<Showquotes/> /!*uncomment this to get quote  code*!/*/}
        <Todo/>
        </header>
    </div>
  );
}

export default App;
