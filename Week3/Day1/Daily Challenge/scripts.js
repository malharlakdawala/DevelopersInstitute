let planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"];
let color = ["red", "blue", "green", "purple", "yellow"];
let moons = [1, 2, 1, 2, 5];

let sectionElements = document.getElementsByClassName("listPlanets")[0];

function showPlanets() {
  for (let i = 0; i < planets.length; i++) {
    let newDiv = document.createElement("div");
    newDiv.className = "planet";
    newDiv.textContent = planets[i];
    newDiv.style.background = color[i];

    let moonDiv = document.createElement("div");
    moonDiv.className = "moon";
    newDiv.appendChild(moonDiv);

    let moonDiv1 = document.createElement("div");
    moonDiv1.className = "moon";
    newDiv.appendChild(moonDiv1);

    sectionElements.appendChild(newDiv);
  }
}

showPlanets();
