const user = require("./scripts.js")
const express = require('express')
const app = express()
// app.use(express.static('public'));

// const user = {
//     firstname: 'John',
//     lastname: 'Doe'
// }

// app.get('/', function (req, res) {
//     res.send(JSON.stringify(user))
// })

// app.get('/', function (req, res) {
//     console.log(user)
//     res.send(JSON.stringify(user))
// })
// app.listen(3000)
//sending data from public/index.html

// const userId = {
//     id:"1234"
// }
//
// app.get('/:id', function (req, res) {
//     console.log(req.params, "req.params")
//     // res.send(`Course ID No. ${req.params.id}`)
//     // res.send(`Course ID No. ${userId["id"]}`)
//     const userID2 = {
//         id:req.params.id
//     }
//     res.send(JSON.stringify(userID2))
// })
const bodyParser = require("body-parser")

app.use(express.static('public'));

app.use(bodyParser.urlencoded({ extended: true }))
app.post('/check', (req, res) => {
    console.log(req.body)
    res.send(req.body)
    // res.send('welcome, ' + req.body.name)
})

app.listen(3000)
