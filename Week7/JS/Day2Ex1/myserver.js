let http = require("http");
const user = require("./main");

// const server = http.createServer(function (req, res) {
//     res.end(`<h1>This is my First Response</h1>
// <h3>This is my First Response</h3>
// <h6>This is my First Response</h6>`)
// }).listen(3000);


const server = http.createServer(function (req, res) {

    // console.log(user)
    res.end(JSON.stringify(user))
}).listen(3000);

