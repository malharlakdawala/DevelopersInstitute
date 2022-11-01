import logo from './logo.svg';
import './App.css';
import Movielist from "./components/movielist";
import Moviedetail from "./components/moviedetail";

function App() {
    return (
        <div className="App">
            <header className="App-header">

                <Movielist/>
                <Moviedetail/>
            </header>
        </div>
    );
}

export default App;
