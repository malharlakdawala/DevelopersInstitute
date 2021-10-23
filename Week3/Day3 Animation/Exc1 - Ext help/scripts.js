let cooking = document.getElementById("cooking");
let advertising = document.getElementById("advertising");
let cookingBtn = document.getElementById("cookingBtn");
let advertisingBtn = document.getElementById("advertisingBtn");

advertisingBtn.addEventListener("click", function () {
  advertising.style.background = "red";
});
cookingBtn.addEventListener("click", function () {
  cooking.style.background = "blue";
});
