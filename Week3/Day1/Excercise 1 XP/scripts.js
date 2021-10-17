// let divId = document.getElementById("navBar");

// divId.setAttribute("id", "socialNetworkNavigation");

// //2
// let ul = document.getElementsByTagName("ul")[0];
// let newLiPosition = document.getElementsByTagName("li")[4];

// let newLiElement = document.createElement("li");
// //let newLiTextNode = document.createTextNode("Logout");
// let newLiHref = document.createElement("a");
// newLiHref.setAttribute("href", "google.com");
// newLiHref.appendChild(document.createTextNode("Logout"));
// newLiElement.appendChild(newLiHref);
// ul.appendChild(newLiElement);

// //3 Bonus
// for (let i = 0; i < document.getElementsByTagName("li").length; i++) {
//   console.log(document.getElementsByTagName("li")[i].textContent);
// }

//Exercise 2 : Users
/*
let newUl = document.getElementsByClassName("list")[0];
newUl.lastElementChild.innerHTML = "Richard";

for (let i = 0; i < document.getElementsByClassName("list").length; i++) {
  document.getElementsByClassName("list")[i].firstElementChild.innerHTML =
    "Malhar";
  let newLi = document.createElement("li");
  let newText = document.createTextNode("Hey Friends");
  newLi.appendChild(newText);
  document.getElementsByClassName("list")[i].appendChild(newLi);
}

document
  .getElementsByClassName("list")[1]
  .removeChild(document.getElementsByClassName("list")[1].childNodes[3]);

document
  .getElementsByClassName("list")[0]
  .setAttribute("class", "list student_list university attendance");

document
  .getElementsByClassName("list")[1]
  .setAttribute("class", "list student_list");
*/
//Exercise 3 : Users And Style
/*
document.getElementsByTagName("div")[0].style.background = "#ADD8E6";

document
  .getElementsByTagName("ul")[0]
  .removeChild(document.getElementsByTagName("ul")[0].childNodes[1]);

document.getElementsByTagName("ul")[0].lastElementChild.style.border =
  "1px solid black";

document.body.style.fontSize = "40px";
*/
function hello() {
  let x = document.getElementsByTagName("ul")[0].firstElementChild.textContent;
  let y = document.getElementsByTagName("ul")[0].lastElementChild.textContent;

  if ((document.getElementsByTagName("div")[0].style.background = "#ADD8E6")) {
    console.log(`Hello ${x} and ${y}`);
  }
}

hello();
