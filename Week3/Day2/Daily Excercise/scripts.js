let r = document.body.firstElementChild;
r.removeChild(r.lastElementChild);

let secondVariable = document.getElementsByTagName("h2")[0];

secondVariable.addEventListener("click", function () {
  secondVariable.style.background = "blue";
});

console.log(document.getElementsByTagName("h1")[0]);

let randNo = Math.floor(Math.random() * 100);
document.getElementsByTagName("h1")[0].style.fontSize = randNo;

document.getElementsByTagName("h3")[0].addEventListener("click", function () {
  document.getElementsByTagName("h3")[0].style.display = "none";
});

let btn = document.createElement("button");
btn.textContent = "Paragraph to bold";
r.appendChild(btn);
btn.addEventListener("click", boldParagraph);

function boldParagraph(e) {
  for (let i = 0; i < document.getElementsByTagName("p").length; i++) {
    document.getElementsByTagName("p")[i].style.fontWeight = "bold";
  }
}
document
  .getElementsByTagName("p")[1]
  .addEventListener("mouseover", function () {
    document.getElementsByTagName("p")[1].style.animation = "fadeinout 3s";
  });

let myForm = document.forms[0];

myForm.addEventListener("submit", printDetails);

let divElement = document.getElementsByClassName("usersAnswer")[0];

let newTable = document.createElement("table");
divElement.appendChild(newTable);

function printDetails(e) {
  e.preventDefault();
  let fnameInput = e.target.elements.fname;
  let lnameInput = e.target.elements.lname;

  let fnameValue = fnameInput.value;
  let lnameValue = lnameInput.value;

  let fOne = document.createElement("tr");
  let lOne = document.createElement("tr");

  let fOneText = document.createTextNode(fnameValue);
  let lOneText = document.createTextNode(lnameValue);

  fOne.appendChild(fOneText);
  lOne.appendChild(lOneText);

  newTable.appendChild(fOne);
  newTable.appendChild(lOne);

  fnameInput.value = "";
  lnameInput.value = "";
}
