let divElement1 = document.body.firstElementChild;
let divElement2 = document.body.children[0];

console.log(divElement1, divElement2);

let ulElement1 = divElement1.nextElementSibling;
let ulElement2 = document.body.children[1];

console.log(ulElement1, ulElement2);

let liElement1 = ulElement1.lastElementChild.textContent;
let liElement2 = ulElement2.children[1].textContent;

liElement2 += " Smith";

console.log(liElement1, liElement2);
