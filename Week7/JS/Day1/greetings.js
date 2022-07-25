// console.log("hi")
const axios = require('axios').default;


let greetings = (name) => {
    console.log(`hello ${name}, how are you`)
}

const getapi = async () => {

    const response = await axios.get("https://jsonplaceholder.typicode.com/users")
    return response
    // console.log(response)
}

module.exports = {greetings, getapi}
