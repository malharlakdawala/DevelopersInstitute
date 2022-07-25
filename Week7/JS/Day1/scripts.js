// console.log("hi")
const {greetings, getapi} = require('./greetings')
let name = "Malhar"

// let greetings = (name) =>{
//     console.log(`hello ${name}, how are you`)
// }
//
// }
const getdata = async () =>{
    console.log(await getapi())
}

getdata()