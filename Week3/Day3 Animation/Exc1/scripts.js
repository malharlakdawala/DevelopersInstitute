// about the green box

// 1. Retrieve the green box
let item = document.getElementById("item");
let item2 = document.getElementById("item2");

item.addEventListener("dragstart", startDragging);
item2.addEventListener("dragstart", startDragging);

function startDragging(event) {
  console.log("start dragging", event.target.id);
  event.target.classList.add("startDragging");
  // console.log(event.dataTransfer)
  // syntax
  // event.dataTransfer.setData("type of data", id of the elem)
  event.dataTransfer.setData("text/plain", event.target.id);
}

// the black target boxes

let allDropZones = document.getElementsByClassName("dropzone");
console.log(allDropZones);

function addTheListeners() {
  for (let zone of allDropZones) {
    zone.addEventListener("dragover", draggingOver);
    zone.addEventListener("drop", dropping);
  }
}

addTheListeners();

// create the dragging Over function
function draggingOver(event) {
  event.preventDefault();
  // console.log(event.target)
  event.target.style.background = "yellow";
}

// Create the dropping function
function dropping(event) {
  event.preventDefault();
  // console.log(event.target)
  // 1. retrieve the element that we want to srop
  let elementToDrop = event.dataTransfer.getData("text/plain");
  // 2. append the element on the drop zone
  let elemNode = document.getElementById(elementToDrop);
  elemNode.style.background = "red";
  event.target.appendChild(elemNode);
}
