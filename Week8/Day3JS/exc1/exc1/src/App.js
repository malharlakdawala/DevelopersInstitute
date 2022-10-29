import logo from './logo.svg';
import './App.css';
import {Routes, Route} from "react-router-dom";
import Home from "./Components/Home";
import About from "./Components/About";
import Shop from "./Components/Shop";
import Navbar1 from "./Components/Navbar";
import "bootstrap/dist/css/bootstrap.min.css";
import PostList from "./Components/PostList";
import content1 from "./content.json"
import APIData from "./Components/APIData";

function App() {

    console.log(content1)
    const content2 = content1

    return (
        <div className="App">
            <Navbar1/>
            <header className="App-header">
                <h1>Welcome to React Router!</h1>
                <Routes>
                    <Route path="/" element={<Home/>}/>
                    <Route path="about" element={<About/>}/>
                    <Route path="shop" element={<Shop/>}/>
                </Routes>
                <PostList data={content2} />
                <APIData/>

            </header>
        </div>
    );
}

export default App;
