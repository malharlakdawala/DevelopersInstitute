/*
let newP = document.createElement("p");
let selectTag = document.getElementsByTagName("genres")[0];
//let newPText = document.createTextNode

let selectID = document.getElementById("genres");
let option3 = document.createElement("option");
selectID.appendChild(option3);
option3.textContent = "Classic";
option3.setAttribute("value", "classic");
selectTag.selectedIndex = 2;

selectID.addEventListener("change", showSelected);

function showSelected(event) {
  event.preventDefault();
  let selectBox = document.getElementById("genres").selectedIndex;
  let selectedValue = document.getElementsByTagName("option")[selectBox].value;
  let pTag = document.createElement("p");
  document.body.append(pTag);
  let pTagcontent = document.createTextNode(selectedValue);
  pTag.appendChild(pTagcontent);
}
*/
/*
let myForm = document.forms[0];

myForm.children[1].addEventListener("click", removecolor);

function removecolor(event) {
  let selectValue = document.getElementById("colorSelect");
  console.log(selectValue.selectedIndex);
  selectValue.remove(selectValue.selectedIndex);
}
*/

//Exercise 3 : Create A Shopping List

let shoppingList = [];

let divElement = document.getElementById("root");
let myForm = document.createElement("form");
divElement.appendChild(myForm);

let textField = document.createElement("input");
textField.setAttribute("id", "inputtext");
let btn = document.createElement("button");
btn.setAttribute("id", "submit");
btn.textContent = "Add Item";

let clr = document.createElement("button");
clr.setAttribute("id", "clear");
clr.textContent = "Clear";

myForm.appendChild(textField);
myForm.appendChild(btn);
myForm.appendChild(clr);

btn.addEventListener("click", addItem);
clr.addEventListener("click", clearAll);

function addItem(event) {
  event.preventDefault();
  console.log("item added");

  if (inputtext.value == "") {
    alert("Enter Value");
    return;
  }
  shoppingList.push(inputtext.value);
  console.log(shoppingList);
  inputtext.value = "";
}

function clearAll(event) {
  event.preventDefault();
  console.log("item cleared");
  shoppingList = [];
  console.log(shoppingList);
}
