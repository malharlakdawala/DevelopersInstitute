let divElement = document.getElementById("container");

for (let i = 0; i < 26; i++) {
  let box = document.createElement("div");
  divElement.appendChild(box);
  box.style.height = "40px";
  box.style.width = "40px";
  box.style.border = "1px solid black";
  box.style.background = "yellow";
  box.setAttribute("draggable", "true");
  box.style.margin = "5px";
}

let pElement = document.getElementsByTagName("p")[0];
