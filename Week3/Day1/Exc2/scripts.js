let divElement1 = document.getElementById("container");
let divElement2 = document.getElementsByTagName("div")[0];

console.log(divElement1, divElement2);

let ulElement1 = document.getElementsByClassName("list");
let ulElement2 = document.getElementsByTagName("ul");

console.log(ulElement1, ulElement2);

let liElement1 = document.getElementsByTagName("li");

console.log(liElement1[0].textContent);

//for (let i = 0; i < ulElement2.length; i++) {
for (let j = 0; j < liElement1.length; j++) {
  console.log(liElement1[j].textContent);
}
//}
