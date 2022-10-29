import React from "react";

const PostList = (props) => {

    let roboAPI = async () => {
        let response = await fetch(`https://jsonplaceholder.typicode.com/users`)
        // console.log("hi")
        let resp = await response.json()
        console.log(resp)
    }



    return (

        props.data.map(item => (
            <div>
                <h2>{item.title}</h2>
                <h3>{item.content}</h3><br/>
            </div>
        ))
    )
}


export default PostList
