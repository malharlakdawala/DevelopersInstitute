const axios = require('axios')
const timedifference =  () =>{
    try {
        console.log("hi")
        const d = new Date(2023, 1, 1);
        // const r = new Date(2022,7,25);
        const r = Date.now()
        e = d - r
        // return (Math.round(e / 86400000))
        return (Math.round(86400000))
    }
    catch (e){
        return e
    }
}

module.exports = timedifference