function number(value) {
  document.getElementById("result").value += value;
}

function equal() {
  var p = document.getElementById("result").value;
  var q = eval(p);
  document.getElementById("result").value = q;
}

function clearscreen() {
  document.getElementById("result").value = "";
}

/*
calculator steps:
1. convert key pushes to display
2. calculate the display
*/
