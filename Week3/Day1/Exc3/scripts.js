// retrieve the div
let divContainer = document.getElementById("container");

// retrieve the h1 inside the div
let allTitle = divContainer.getElementsByTagName("h1");

let allTitle2 = document.getElementById("container").getElementsByTagName("h1");

// retrieve with querySelector

let divFirstContainer = document.querySelector("#container");
console.log(divFirstContainer);

// retrieve the first element that matches the selection
let firstTitle = document.querySelector("#container > h1");
console.log(firstTitle);

let allTitleSelector = document.querySelectorAll("#container > h1");
console.log(allTitleSelector[1]);
