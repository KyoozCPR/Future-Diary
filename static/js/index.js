var acc = document.getElementsByClassName("accordion");
const slider = document.getElementById('slider');
const popup_element = document.getElementById("popup");
const play_button = document.getElementById("open");
const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".character-navbar");
var i;

function OpenPopup() {
  
  popup_element.style = "display: block; z-index: 1";
  play_button.style = "display: none; z-index: 0";
}

function ClosePopup() {

  play_button.style = "display: block; z-index: 1";
  popup_element.style = "display: none; z-index: 0";
}



hamburger.addEventListener("click", mobileMenu);

function mobileMenu() {
    hamburger.classList.toggle("activate");
    navMenu.classList.toggle("activate");

}


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