// let fetchusers = async () => {
//     try {
//         const response = await fetch("https://jsonplaceholder.typicode.com/users")
//         const users = await response.json()
//         console.log(users)
//     } catch (e) {
//         console.log(e)
//     }
// }

// const { timeout } = require("async");

// // fetchusers()

// console.log("1");
// async function swapi() {
//   try {
//     let response = await fetch("https://www.swapi.tech/api/starships/9/");
//     result = await response.json();
//     console.log(result.result.properties.model);
//   } catch (e) {
//     console.log(e);
//   }
// }
// swapi();
// console.log("2");

// function resolveAfter2Seconds() {
//   return new Promise((resolve) => {
//     setTimeout(() => {
//       resolve("resolved");
//     }, 2000);
//   });
// }

// async function asyncCall() {
//   console.log("calling");
//   let result = await resolveAfter2Seconds();
//   console.log(result);
// }

// asyncCall();

// let resolveAfter2Seconds = function () {
//   console.log("starting slow promise");
//   return new Promise((resolve) => {
//     setTimeout(function () {
//       resolve("slow");
//       console.log("slow promise is done");
//     }, 2000);
//   });
// };

// let resolveAfter1Second = function () {
//   console.log("starting fast promise");
//   return new Promise((resolve) => {
//     setTimeout(function () {
//       resolve("fast");
//       console.log("fast promise is done");
//     }, 1000);
//   });
// };

// let sequentialStart = async function () {
//   console.log("==SEQUENTIAL START==");
//   const slow = await resolveAfter2Seconds();
//   console.log(slow);
//   const fast = await resolveAfter1Second();
//   console.log(fast);
// };

// sequentialStart();

// let resolveAfter2Seconds = function () {
//   console.log("starting slow promise");
//   return new Promise((resolve) => {
//     setTimeout(function () {
//       resolve("slow");
//       console.log("slow promise is done");
//     }, 2000);
//   });
// };

// let resolveAfter1Second = function () {
//   console.log("starting fast promise");
//   return new Promise((resolve) => {
//     setTimeout(function () {
//       resolve("fast");
//       console.log("fast promise is done");
//     }, 1000);
//   });
// };

// let concurrentStart = async function () {
//   console.log("==CONCURRENT START with await==");
//   const slow = resolveAfter2Seconds();
//   const fast = resolveAfter1Second();
//   console.log(await slow);
//   console.log(await fast);
// };

// setTimeout(concurrentStart, 4000);

// const urls = [
//   "https://jsonplaceholder.typicode.com/users",
//   "https://jsonplaceholder.typicode.com/posts",
//   "https://jsonplaceholder.typicode.com/albums",
// ];

// const getData = async function () {
//   const [users, posts, albums] = await Promise.all(
//     urls.map((url) => fetch(url).then((resp) => resp.json()))
//   );
//   console.log("users", users);
//   console.log("posta", posts);
//   console.log("albums", albums);
// };

// const getData = async function (i) {
//   return fetch(urls[i]);
// };

// async function iniate() {
//   for (i = 0; i < urls.length; i++) {
//     result = await getData(i);
//     console.log(urls[i], result);
//   }
// }
// iniate();

// let makeAllCaps = async (arr) => {
//   let resp_arr = [];
//   for (i = 0; i < arr.length; i++) {
//     if (typeof arr[i] === "string") {
//       resp_arr.push(arr[i].toUpperCase());
//     }
//   }
//   return resp_arr;
// };

// let sortWords = async (arr) => {
//   let resp_arr = [];
//   for (i = 0; i < arr.length; i++) {
//     if (arr[i].length > 4) {
//       resp_arr.push(arr[i]);
//     }
//   }
//   return resp_arr.sort();
// };

// let main = async () => {
//   try {
//     result = await makeAllCaps([1, "pear", "mango", 5, "papaya", "banana"]);
//     result = await sortWords(result);
//     console.log(result);
//   } catch (e) {
//     console.log("error idhar aaya", e);
//   }
// };
// main();

// const form = document.getElementById("form");
// // if (form) {
// form.addEventListener("submit", function (e) {
//   // Prevent default behavior:
//   e.preventDefault();
//   // Create payload as new FormData object:
//   console.log("he");
//   const formData = new FormData(form);
//   // Convert formData object to URL-encoded string:
//   const payload = new URLSearchParams(formData);
//   fetch("https://httpbin.org/post", {
//     method: "POST",
//     body: payload,
//   })
//     .then((res) => res.json())
//     .then((data) => console.log(data));
// });
// // }

let getSunriseData = async (lat1, long1) => {
  result =  fetch(
    `https://api.sunrise-sunset.org/json?lat=${lat1}&lng=${long1}`
  );

  console.log("resul1", result);
  return result;
};

async function showData() {
  // console.log("hi");
  var lat1 = document.getElementById("lat1").value;
  var long1 = document.getElementById("long1").value;
  document.write(lat1);
  result = await getSunriseData(lat1, long1);
  console.log(result);
}
