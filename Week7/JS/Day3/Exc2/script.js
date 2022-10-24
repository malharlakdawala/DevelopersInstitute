const express = require('express')
// import express from 'express';
// import fetch from 'node-fetch'

// const fetch = require('node-fetch')

const app = express()
app.use(express.static('public'));

app.get('/', function (req, res) {
  res.send('Hello World')
})

// let roboAPI = async () => {
//     let response = await fetch(`https://jsonplaceholder.typicode.com/users`)
//     // console.log("hi")
//     let resp = await response.json()
//     return resp
// }
//
// let mainSection = document.getElementById("main_section")
// let dataShow = (val) => {
//     console.log(val.name, val.id)
//     let smallSection = document.createElement("div")
//     let imageSection = document.createElement("img")
//     let smallSectionBelow = document.createElement("span")
//     let imageURL = "https://robohash.org/".concat(val.name)
//     imageSection.setAttribute("src", imageURL)
//     smallSection.style.border = "2px solid black"
//     smallSection.style.padding = "10px"
//     mainSection.style.width = "250px"
//     imageSection.style.height = "150px"
//     smallSectionBelow.innerText = `
//     Name: ${val.name}
//     id: ${val.id}
//     username: ${val.username}
//     email: ${val.email}`
//     smallSection.style.textAlign="center"
//     smallSection.style.margin="15px"
//     smallSection.appendChild(imageSection)
//     smallSection.appendChild(smallSectionBelow)
//     mainSection.appendChild(smallSection)
// }
//
// let showData = async () => {
//     let users = await roboAPI()
//     console.log("hello ", users)
//     users.forEach(dataShow)
//
// }
// showData()

let apiData = "hello"
module.exports = apiData

// app.post('/search', function (req, res) {
//   res.send('POST request to the homepage')
// })


app.listen(3000)
