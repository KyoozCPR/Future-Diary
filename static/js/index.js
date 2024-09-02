var acc = document.getElementsByClassName("accordion");
const slider = document.getElementById('slider');
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}



function characters() {
    document.getElementById("slider-container").scrollIntoView({behavior: 'smooth'});
}
function sinistra() {
    slider.scrollBy({
        left: -slider.clientWidth / 2,
        behavior: 'smooth'
    });
}
function scrollRight() {
    slider.scrollBy({
        left: slider.clientWidth / 2,
        behavior: 'smooth'
    });
}