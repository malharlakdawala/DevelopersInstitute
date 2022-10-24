import React from 'react';

const UserFavoriteColors = (props) => {
    return (

        props.fav_animals.map((item, i) => {
            return (
            <li>{props.fav_animals[i]}</li>
            )
        })
    )
}

export default UserFavoriteColors