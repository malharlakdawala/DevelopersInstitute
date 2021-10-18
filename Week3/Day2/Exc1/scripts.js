// document
//   .getElementById("red")
//   .addEventListener("", backgroundColorChange("red"));
// document
//   .getElementById("blue")
//   .addEventListener("click", backgroundColorChange("blue"));

// function backgroundColorChange(color) {
//   console.log(color);
//   document.body.style.background = color;
// }

document.getElementById("red").addEventListener("click", function () {
  document.body.style.background = "red";
});

document.getElementById("blue").addEventListener("click", function () {
  document.body.style.background = "blue";
});
