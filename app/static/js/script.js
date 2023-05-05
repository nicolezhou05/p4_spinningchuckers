// NAVBAR
// Get the navbar
var navbar = document.querySelector('.navbar');

// Get the links inside the navbar
var links = navbar.querySelectorAll('a');

// Loop through each link and add a click event listener
for (var i = 0; i < links.length; i++) {
  links[i].addEventListener('click', function() {
    // Remove the active class from all links
    for (var j = 0; j < links.length; j++) {
      links[j].classList.remove('active');
    }
    // Add the active class to the clicked link
    this.classList.add('active');
  });
}