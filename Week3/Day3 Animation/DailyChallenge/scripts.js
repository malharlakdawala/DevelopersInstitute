/*
let txt = document.getElementById("textfield");

txt.addEventListener("keyup", chkcharacter);

function chkcharacter(event) {
  let char = event.key;
  console.log(char);
  let regex = /^[A-Za-z]+$/;
  if (!regex.test(char)) {
    event.target.value = event.target.value.slice(0, -1);
  }
}
*/
let txt = document.getElementById("textfield");

txt.addEventListener("keydown", chkcharacter);

function chkcharacter(event) {
  let char = event.key;
  console.log(char);
  let regex = /^[A-Za-z]+$/;
  if (!regex.test(char)) {
    event.preventDefault();
  }
}
