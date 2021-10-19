function myMove() {
  var timer = setInterval(function () {
    console.log("hi");
    let animateBox = document.querySelector("#animate");
    let containerBox = document.querySelector("#container");

    if (animateBox.offsetTop < 340) {
      animateBox.style.top = animateBox.offsetTop + 8 + "px";
      animateBox.style.left = animateBox.offsetTop + 8 + "px";
      console.log(animateBox.offsetTop);
    } else {
      clearInterval(timer);
    }
  }, 10);
}
