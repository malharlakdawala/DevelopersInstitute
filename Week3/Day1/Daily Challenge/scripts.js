let planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"];
let color = ["orange", "blue", "green", "purple", "yellow"];
let moons = [5, 2, 1, 2, 5];

let sectionElements = document.getElementsByClassName("listPlanets")[0];

function showPlanets() {
  for (let i = 0; i < planets.length; i++) {
    let newDiv = document.createElement("div");
    newDiv.className = "planet";
    // newDiv.textContent = planets[i] + "\n";
    newDiv.style.background = color[i];

    for (let j = 0; j < moons[i]; j++) {
      let moonDiv = document.createElement("div");
      moonDiv.className = "moon";
      newDiv.appendChild(moonDiv);
    }

    sectionElements.appendChild(newDiv);
  }
}

showPlanets();
