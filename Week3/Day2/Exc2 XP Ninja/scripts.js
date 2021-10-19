/*
function calculateTip() {
  myForm = document.forms[0];
  let billAmount = document.getElementById("billamt");
  let serviceQuality = document.getElementById("serviceQual");
  let numberOfPeople = document.getElementById("peopleamt");

  if (billAmount.value == 0 || serviceQuality.value == "") {
    alert("Enter Value");
  }
  if (numberOfPeople.value < 2) {
    numberOfPeople.value = 1;
    let eachTag = document.getElementById("each");
    eachTag.remove(eachTag);
  }
  let total = (billAmount.value * serviceQuality.value) / numberOfPeople.value;
  total = total.toFixed(2);
  document.getElementById("totalTip").style.display = "block";
  document.getElementById("tip").textContent = total;
  console.log(billAmount.value, serviceQuality.value, numberOfPeople.value);
}

document.getElementById("calculate").addEventListener("click", calculateTip);
*/
//Exercise 2 : Validate The Email
/*
document.getElementById("submit").addEventListener("click", validateEmail);

function validateEmail(event) {
  event.preventDefault();
  let email = document.getElementById("email");
  //let email1 = event.target.elements.email;
  console.log(email.value);
  let validRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

  if (email.value.match(validRegex)) {
    console.log("email valid");
    email.value = "";
    return;
  } else alert("Invalid email");
}
*/

//Exercise 3 : Get The User’s Geolocation Coordinates
document.getElementById("submit").addEventListener("click", geoloc);
var x = document.getElementById("demo");

function geoloc() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML =
    "Latitude: " +
    position.coords.latitude +
    "<br>Longitude: " +
    position.coords.longitude;
}
