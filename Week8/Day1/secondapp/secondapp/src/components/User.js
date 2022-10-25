import React from "react";

const User = (props) => {
    // console.log(props)
    const {user} = props;
    const {name, username, email, address, id} = user;
    return (
        <React.Fragment>
            <div className="tc grow bg-light-blue br3 pa2 ma2 dib bw2 shadow-2">
                <h2>User Info:</h2>
                <h4>{name}</h4>
                <p>{username}</p>
                <p>{email}</p>
                <p>{address.city}</p>
                <p>Id = {id}</p>
                <img src={`https://robohash.org/${id}`}/>
            </div>
        </React.Fragment>
    )
}

export default User