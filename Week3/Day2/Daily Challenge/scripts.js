document.getElementById("lib-button").addEventListener("click", madLibs);

let btn = document.createElement("button");
btn.textContent = "Shuffle";
btn.setAttribute("id", "shuffle");
let newPelement = document.createElement("p");
document.body.children[3].appendChild(newPelement);
newPelement.appendChild(btn);
document.getElementById("shuffle").addEventListener("click", shuffle);

function madLibs(event) {
  let inputText = ["noun", "adjective", "person", "verb", "place"];
  let noun = document.getElementById("noun").value;
  var words = [];

  for (let i = 0; i < inputText.length; i++) {
    words[i] = document.getElementById(inputText[i]).value;

    if (words[i] == "") {
      alert("please input all the fields");
      return;
    }
  }
  let sentence = words.join(" ");
  console.log(sentence);
  let pElement = document.getElementById("story");
  pElement.appendChild(document.createTextNode(sentence));

  document.getElementById("shuffle").addEventListener("click", shuffle);
}

function shuffle(event) {
  if (event.detail === 3) {
    let inputText = ["noun", "adjective", "person", "verb", "place"];
    let noun = document.getElementById("noun").value;
    var words = [];

    for (let i = 0; i < inputText.length; i++) {
      words[i] = document.getElementById(inputText[i]).value;

      if (words[i] == "") {
        alert("please input all the fields");
        return;
      }
    }
    let randomIndex = 0;
    let sentence = [];
    for (let i = words.length; i > 0; i--) {
      randomIndex = Math.floor(Math.random() * i);
      [words[randomIndex], words[i]] = [words[i], words[randomIndex]];
    }
    console.log(words.join(" "));

    newPelement.appendChild(document.createTextNode(words));
  }
}
