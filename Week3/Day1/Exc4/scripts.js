let names = ["John", "Lola", "Tom"];
let divContainer = document.getElementById("container");

function addStudents() {
  //create a paragraph PER name

  for (let index = 0; index < names.length; index++) {
    // create a paragraph
    let newP = document.createElement("p");
    // create a text node, with the value = to the name of the student
    let newText = document.createTextNode(names[index]);
    // add the newText to the newP
    newP.appendChild(newText);
    // add the newP to the divcontainer
    divContainer.appendChild(newP);
    // style the paragraph
    newP.style.backgroundColor = "yellow";
    newP.style.fontSize = "25px";
  }
}
addStudents();

let color = ["red", "blue", "green"];

function addH1Elements() {
  let newH1 = document.createElement("h1");
  let newH1elements = document.createTextNode(color[0]);
  newH1.appendChild(newH1elements);
  divContainer.appendChild(newH1);
  newH1.style.backgroundColor = "Red";
}
addH1Elements();
