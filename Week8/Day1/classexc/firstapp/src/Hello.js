
//
// function Hello() {
//     return (
//         <div>
//             <h1>Hello from Hello.js</h1>
//             <Button variant="primary">Primary</Button>{' '}
//             <Button variant="secondary">Secondary</Button>{' '}
//             <Button variant="success">Success</Button>{' '}
//             <Button variant="warning">Warning</Button>{' '}
//             <Button variant="danger">Danger</Button>{' '}
//             <Button variant="info">Info</Button>{' '}
//             <Button variant="light">Light</Button>{' '}
//             <Button variant="dark">Dark</Button> <Button variant="link">Link</Button>
//
//         </div>
//     )
// }
//
// export default Hello
import React from 'react';

import './App.css';
import UserFavoriteColors from './UserFavoriteColors';

function Hello() {
    const user = {
        first_name: 'Bob1',
        last_name: 'Dylan',
        fav_animals: ['Horse', 'Turtle', 'Elephant', 'Monkey']
    };

    return (
        <div className="Hello">
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

export default Hello;
