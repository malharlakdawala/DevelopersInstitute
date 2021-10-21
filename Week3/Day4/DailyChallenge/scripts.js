let listTasks = [];
document.getElementById("submit").addEventListener("click", addTask);
let divElement = document.getElementsByClassName("listTasks");

function addTask(event) {
  event.preventDefault();
  let textData = document.getElementById("textfield");
  if (textData.value == "") {
  } else {
    listTasks.push(textData.value);

    document
      .createTextNode(textData.value)
      .appendChild(document.createElement("p"));

    document
      .getElementsByClassName("listTasks")
      .appendChild(document.createTextNode(textData.value));

    textData.value = "";
    console.log(listTasks);
  }
}
