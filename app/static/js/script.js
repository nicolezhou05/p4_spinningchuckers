// NAVBAR
// Get the navbar
var navbar = document.querySelector('.navbar');

// Get the links inside the navbar
var links = navbar.querySelectorAll('.navtab');

// Gets an array of all the tabs
var tabs = document.querySelectorAll(".tab");

// Loop through each link and add a click event listener
for (var i = 0; i < links.length; i++) {
  links[i].addEventListener('click', function() {
    // Remove the active class from all links
    for (var j = 0; j < links.length; j++) {
      links[j].classList.remove('active');
    }
    // Add the active class to the clicked link
    this.classList.add('active');

    // Changes the current tab showing
    for (var c = 0; c < tabs.length; c++) {
      var current = tabs[c];
      // Loop through each tab and check if they have the class selected
      // Compares the classname with the innerHTML of the navbar tab
      if (current.id == `${this.innerHTML.toLowerCase()}` && current.classList.contains('hidden')) {
        current.classList.remove('hidden');
      }
      else {
        current.classList.add('hidden');
      }
    }
  });
}
