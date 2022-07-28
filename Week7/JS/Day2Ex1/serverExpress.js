const express = require('express')
const app = express()

app.get('/', function (req, res) {
  // res.send('Hello World')
res.send(`<h1>Hello World1</h1>
<h2>Hello world 2</h2>`)
})


app.listen(3000)
