import logo from './logo.svg';
import './App.css';
import { Routes, Route } from "react-router-dom";
import Home from "./Components/Home";
import About from "./Components/About";
import Shop from "./Components/Shop";
import Navbar from "./Components/Navbar";

function App() {
    return (
        <div className="App">
            <Navbar/>
            <header className="App-header">
                <h1>Welcome to React Router!</h1>
                <Routes>
                    <Route path="/" element={<Home/>}/>
                    <Route path="about" element={<About/>}/>
                    <Route path="shop" element={<Shop/>}/>
                </Routes>
            </header>
        </div>
    );
}

export default App;
