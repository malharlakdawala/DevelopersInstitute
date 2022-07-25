let http = require("http");
const {largeNumber, hello,currentDate}= require('./main.js')

// const server = http.createServer( () => {
//    console.log('I am listening....');
// });
// server.listen(3000);

const server = http.createServer(function (req, res) {
    console.log('I am listening....');
    res.writeHead(200);
    // res.end(Date.now());

    if(req.url == '/') {
        res.end("<h1>this is the frontend</h1>");
    } else if(req.url == '/about') {
        res.end("<h1>this is the about</h1>");
        h=currentDate()
        console.log(h)
    } else {
        res.end("<h1>Page not found 404</h1>");

    }

}).listen(3000);
