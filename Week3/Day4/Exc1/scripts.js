let gridElement = document.getElementById("rightGrid");

for (let i = 0; i < 1800; i++) {
  let gridDivs = document.createElement("div");
  gridElement.appendChild(gridDivs);
  gridDivs.style.border = "0.01px solid grey";
  gridDivs.style.background = "white";
  gridDivs.style.gridAutoRows = "auto";
  gridDivs.style.gridAutoColumns = "auto";
  gridDivs.setAttribute("id", "gridCanvasDiv");
}

let colorArray = [
  "#FF6633",
  "#FFB399",
  "#FF33FF",
  "#FFFF99",
  "#00B3E6",
  "#E6B333",
  "#3366E6",
  "#999966",
  "#99FF99",
  "#B34D4D",
  "#80B300",
  "#809900",
  "#E6B3B3",
  "#6680B3",
  "#66991A",
  "#FF99E6",
  "#CCFF1A",
  "#FF1A66",
  "#E6331A",
  "#33FFCC",
  "#66994D",
  "#B366CC",
  "#4D8000",
  "#B33300",
  "#CC80CC",
  "#66664D",
  "#991AFF",
  "#E666FF",
  "#4DB3FF",
  "#1AB399",
];
let colorElement = document.getElementById("colorPalette");
for (let i = 0; i < 18; i++) {
  let gridDivs = document.createElement("div");
  colorElement.appendChild(gridDivs);
  gridDivs.style.border = "1px solid black";
  gridDivs.style.background = colorArray[i];
  gridDivs.style.gridAutoRows = "auto";
  gridDivs.style.gridAutoColumns = "auto";
  gridDivs.setAttribute("id", "colorDiv");
}
document.body.addEventListener("click", check);

let temp = "";

function check(event) {
  if (event.target.id == "colorDiv") {
    console.log(event.target.style.background);
    temp = event.target.style.background;
  } else if (event.target.id == "gridCanvasDiv") {
    console.log("gridCanvasDiv");
    event.target.style.background = temp;
  } else if (event.target.id == "clrButton") {
    console.log("clr");
    for (let i = 0; i < 1800; i++) {
      document.getElementById("gridCanvasDiv").style.background = "white";
      //not working for now
    }
  }
}
let isMouseDown = false;
document.body.addEventListener("mousedown", function (event) {
  if (event.target.id == "gridCanvasDiv") {
    isMouseDown = true;
  }
});

document.body.addEventListener("mouseup", function (event) {
  if (event.target.id == "gridCanvasDiv") {
    isMouseDown = false;
  }
});

document.body.addEventListener("mouseover", function (event) {
  if (event.target.id == "gridCanvasDiv" && isMouseDown) {
    event.target.style.background = temp;
  }
});
