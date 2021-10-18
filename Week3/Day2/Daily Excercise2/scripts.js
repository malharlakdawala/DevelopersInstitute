/*
function getBold_items() {
  let boldItems = document.getElementsByTagName("strong");
}

function highlight() {
  let boldItems = document.getElementsByTagName("strong");
  for (let i = 0; i < boldItems.length; i++) {
    boldItems[i].style.color = "blue";
  }
}

function return_normal() {
  let boldItems = document.getElementsByTagName("strong");
  for (let i = 0; i < boldItems.length; i++) {
    boldItems[i].style.color = "black";
  }
}
document.body.firstElementChild.addEventListener("onmouseover", highlight);

document
  .getElementsByTagName("p")[0]
  .addEventListener("onmouseout", return_normal);
*/

let divElement = document.body.firstElementChild;

let myForm = document.forms[0];

myForm.addEventListener("submit", calculateVolume);

function calculateVolume(event) {
  event.preventDefault();
  let radius = event.target.elements.radius.value;
  let voulme = event.target.elements.volume;

  let radiusValue = radius.value;
  let sphereVolume = 4 * 3.14 * radius * radius * radius;

  console.log(sphereVolume);

  let sphereVolumeP = document.createElement("p");
  let sphereVolumeText = document.createTextNode(sphereVolume);

  sphereVolumeP.appendChild(sphereVolumeText);

  divElement.appendChild(sphereVolumeP);
  event.target.elements.radius.value = "";
  event.target.elements.volume.value = "";
}
