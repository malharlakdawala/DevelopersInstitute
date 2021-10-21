let drag = document.getElementById("drag1");
let drop = document.querySelector(".dropzone");

let tempStorage = null;

drag.addEventListener("dragstart", function (e) {
  tempStorage = e.target;
});

drop.addEventListener("dragover", function (e) {
  e.preventDefault();
});

drop.addEventListener("drop", function (e) {
  if (tempStorage) {
    e.target.appendChild(tempStorage);
  }
});
