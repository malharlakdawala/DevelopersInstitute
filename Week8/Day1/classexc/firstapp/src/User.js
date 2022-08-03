import React from "react";
const User = (props) => {
    console.log(props)
    return (
        <React.Fragment>
            <h2>User Info:</h2>
            <h4>{props.name}</h4>
            <p>{props.username}</p>
            <p>{props.email}</p>

        </React.Fragment>
    )
}

export default User