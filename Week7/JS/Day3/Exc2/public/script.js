const apiData = require('../script.js')

// const roboAPI = () =>{
//     fetch("https://jsonplaceholder.typicode.com/users")
//         .then(resp => resp.json())
//         .then(resp=> console.log(resp))
//         .catch(function (err){
//             console.log(err)
//         })
// }

// const roboAPI = () => {
//     fetch("https://jsonplaceholder.typicode.com/users")
//         .then((response) => {
//             return response.json().then((data) => {
//                 // console.log(data);
//                 return data;
//             }).catch((err) => {
//                 console.log(err);
//             })
//         });
// }
// let jsonData
// hello = roboAPI().then((data) => {
//     jsonData = data;
// })
//
// console.log("ths reop", hello)


//   function getvals(){
//     return fetch('https://jsonplaceholder.typicode.com/posts',
//     {
//     	method: "GET",
//       headers: {
//         'Accept': 'application/json',
//         'Content-Type': 'application/json',
//       },
//     })
//     .then((response) => response.json())
//     .then((responseData) => {
//       // console.log(responseData);
//       return responseData;
//     })
//     .catch(error => console.warn(error));
//   }
// let user={"hello":"asd"}
//   // getvals().then(response => console.log("hello ",response));
//   getvals().then(response => {
//       user = response
//   });
// console.log("Asda ", user)

// let roboAPI = async () => {
//     let response = await fetch(`https://jsonplaceholder.typicode.com/users`)
//     // console.log("hi")
//     resp = await response.json()
//     return resp
// }
//
// let dataShow = (val) => {
//     console.log(val.name)
//     let mainSection = document.getElementById("main_section")
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
//     console.log(apiData)
// }
//
// let showData = async () => {
//     users = await roboAPI()
//     console.log("hello ", users)
//     users.forEach(dataShow)
//
// }
// showData()
//
console.log(apiData)