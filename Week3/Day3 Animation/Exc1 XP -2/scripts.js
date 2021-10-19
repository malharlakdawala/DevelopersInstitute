let smallBox = document.querySelector(".smallBox");
let bigBox = document.querySelector(".bigBox");

smallBox.addEventListener("dragstart", dragstart);
smallBox.addEventListener("dragend", dragstop);

function dragstart() {
  this.className += " smalBoxDuringDrag";
  // setTimeout(function () {
  //   this.className = "smallBoxAfterDrag";
  // }, 0);
  //this.className = "smallBoxAfterDrag";
  setTimeout(() => (this.className = "smallBoxAfterDrag"), 0);
}

function dragstop() {
  this.className = "smallBox";
}

bigBox.addEventListener("dragover", dragover);
bigBox.addEventListener("dragenter", dragenter);
bigBox.addEventListener("dragleave", dragnleave);
bigBox.addEventListener("drop", dragDrop);

function dragover(e) {
  e.preventDefault();
  console.log("dragover");
}

function dragenter(e) {
  e.preventDefault();
  this.className += " bigBoxHover";
  console.log("dragenter");
}

function dragnleave() {
  this.className = "bigBox";
  console.log("draleave");
}

function dragDrop() {
  this.className += " .bigBoxAfterDrop";
  this.append(smallBox);
  console.log("dragdrop");
}
