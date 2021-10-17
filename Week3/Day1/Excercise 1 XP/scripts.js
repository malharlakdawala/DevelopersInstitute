let divId = document.getElementById("navBar");

divId.setAttribute("id", "socialNetworkNavigation");

//2
let ul = document.getElementsByTagName("ul")[0];
let newLiPosition = document.getElementsByTagName("li")[4];

let newLiElement = document.createElement("li");
//let newLiTextNode = document.createTextNode("Logout");
let newLiHref = document.createElement("a");
newLiHref.setAttribute("href", "google.com");
newLiHref.appendChild(document.createTextNode("Logout"));
newLiElement.appendChild(newLiHref);
ul.appendChild(newLiElement);
