var express = require('express')
var bodyParser = require('body-parser')
const itemList = require("./script.js")

var app = express()
app.use(express.static('public'));

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({extended: true}))


app.get('/items', function (req, res) {
    console.log(itemList)
    // res.send(JSON.stringify(itemList))
    res.send(itemList)
})

app.get('/items/:id', function (req, res) {
    if (req.params.id < itemList.length + 1) {
        let itemFilter = itemList.filter(items => items.id == req.params.id)
        console.log(itemFilter)
        res.send(itemFilter)
        res.status(200)

    } else {
        res.status(404)
        res.send("Item Not Found")
    }
    // res.send(items)
    // console.log(itemList.id)
    // res.send(JSON.stringify(itemList))
    // res.send(itemList)
})

app.post("/itemadd", function (req,res){
    newItem={
        id: itemList.length+1,
        name:req.body.itemname,
        price:req.body.itemprice
    }
    itemList.push(newItem)
    res.send(itemList)

})

app.listen(3000)
