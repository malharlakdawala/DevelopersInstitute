import './App.css';
import UserFavoriteColors from "./UserFavoriteColors";

function App() {
    const user = {
        first_name: 'Bob',
        last_name: 'Dylan',
        fav_animals: ['Horse', 'Turtle', 'Elephant', 'Monkey']
    };

    return (
        <div className="App">
            <header className="App-header">
                {
                    <h3>{user.first_name}</h3>
                }
                {
                    <h3>{user.last_name}</h3>
                }


                <UserFavoriteColors fav_animals={user.fav_animals}/>

            </header>
        </div>

    );
}

export default App;
