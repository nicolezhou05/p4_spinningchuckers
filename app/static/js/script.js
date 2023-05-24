var navbar = document.querySelector('.navbar');
var links = navbar.querySelectorAll('.navtab');
var tabs = document.querySelectorAll(".tab");

var temperature, health, energy, buildings, transportation, jobs;
function initialize(tem, hea, ene, bui, tra, job) {
  temperature = JSON.stringify(tem);
  health = JSON.stringify(hea);
  energy = JSON.stringify(ene);
  buildings = JSON.stringify(bui);
  transportation = JSON.stringify(tra);
  jobs = JSON.stringify(job);
}

for (var i = 0; i < links.length; i++) {
  links[i].addEventListener('click', function() {
    for (var j = 0; j < links.length; j++) {
      links[j].classList.remove('active');
    }
    this.classList.add('active');

    for (var c = 0; c < tabs.length; c++) {
      var current = tabs[c];
      if (current.id == `${this.innerHTML.toLowerCase()}` && current.classList.contains('hidden')) {
        current.classList.remove('hidden');
      }
      else if (current.id != `${this.innerHTML.toLowerCase()}`) {
        current.classList.add('hidden');
      }
    }
  });
}

var map = L.map('map').setView([40.7142, -74], 14);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: 'Map data © OpenStreetMap contributors',
  maxZoom: 20,
  minZoom: 12
}).addTo(map);

markers = [];

function onMapClick(e) {
  const { lat, lng } = e.latlng;
  clearMarkers();
  addMarker(lat, lng);
}

function addMarker(lat, lng) {
  const marker = L.marker([lat, lng]).addTo(map);
  markers.push(marker);
}

function clearMarkers() {
  markers.forEach(marker => marker.remove());
  markers = [];
}

addMarker(40.7128, -74.0060);

map.on('click', onMapClick);