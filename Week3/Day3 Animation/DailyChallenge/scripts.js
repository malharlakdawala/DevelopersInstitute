let txt = document.getElementById("textfield");

txt.addEventListener("keyup", chkcharacter);

function chkcharacter(event) {
  let char = event.key;
  let regex = /^[A-Za-z]+$/;
  if (!regex.test(char)) {
    event.target.value = event.target.value.slice(0, -1);
  }
}
//default behaviour of keydown

// function removeCharacter() {
//   txt.addEventListener("keyup", function (event) {
//     event.target.value = event.target.value.slice(0, -1);
//     console.log("d");
//     return;
//   });
//   return;
// }
