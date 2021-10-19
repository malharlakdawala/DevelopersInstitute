let btn = document.getElementsByTagName("a")[0];
let divElement = document.getElementById("container");

//btn.addEventListener("click", addblocks);

function addblocks() {
  console.log("d");
  let d = document.createElement("div");
  d.style.background = "rgb(0, 222, 207)";
  d.style.width = "100px";
  d.style.height = "100px";
  divElement.appendChild(d);
}

btn.addEventListener("click", addblocks);
