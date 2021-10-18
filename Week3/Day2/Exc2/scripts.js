let color = ["red", "blue", "green", "yellow"];

let d = document.body.firstElementChild;

let r = document.createElement("button");
r.setAttribute("id", "blue");
r.textContent = "blue";
d.appendChild(r);

r.addEventListener("click", changeColor);

function changeColor(event) {
  console.log(event);
}
