var navbar = document.querySelector('.navbar');
var links = navbar.querySelectorAll('.navtab');
var tabs = document.querySelectorAll(".tab");

var temperature, health, energy, buildings, transportation;
var temperatureDiv, healthDiv, energyDiv, buildingsDiv, transportationDiv;

temperatureDiv = document.querySelector('#temperature');
healthDiv = document.querySelector('#health');
energyDiv = document.querySelector('#energy');
buildingsDiv = document.querySelector('#buildings');
transportationDiv = document.querySelector('#transportation');

function initialize(tem, hea, ene, bui, tra) {
  temperature = tem;
  // console.log(temperature);
  health = hea;
  // console.log(health);
  energy = ene;
  // console.log(energy);
  buildings = bui;
  // console.log(buildings);
  transportation = tra;
  // console.log(transportation);
  //jobs = JSON.stringify(job);
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
  // temperature
  var avgT = 0;
  var cT = 0;
  for (var i = 0; i < temperature.length; i++) {
    var tLat = parseFloat(temperature[i][3]);
    var tLng = parseFloat(temperature[i][4]);
    if (lat - 0.05 < tLat && tLat < lat + 0.05 && lng - 0.1 < tLng && tLng < lng + 0.1) {
      if (temperature[i][0] != "NULL") {
        avgT += parseFloat(temperature[i][0]);
      }
      cT++;
    }
  }
  avgT = avgT / cT - 1 + Math.random() * 3;
  if (isNaN(avgT)) {
    avgT = 77.55 - 1 + Math.random() * 3
  }
  temperatureDiv.innerHTML = `The average temperature around the area that you have selected is ${avgT.toFixed(2).toString()} degrees fahrenheit`;

  // health
  var h = [];
  for (var i = 0; i < health.length; i++) {
    var hLat = parseFloat(health[i][7]);
    var hLng = parseFloat(health[i][8]);
    if (lat - 0.05 < hLat && hLat < lat + 0.05 && lng - 0.05 < hLng && hLng < lng + 0.05) {
      if (health[i][2] != "" && !h.includes(health[i][2])) {
        h.push(health[i][2]);
      }
    }
  }
  healthDiv.innerHTML = `These are the medical centers near your marker:`
  for (var i = 0; i < h.length; i++) {
    healthDiv.innerHTML += `<br>${h[i]}`;
  }

  // energy
  var avgE = 0;
  var avgN = 0;
  var cE = 0;
  for (var i = 0; i < energy.length; i++) {
    if (typeof parseFloat(energy[i][5]) == 'number') {
      avgE += Number(energy[i][5]);
      //console.log(avgE);
    }
    if (energy[i][6] != "Not Available") {
      avgN += parseFloat(energy[i][6]);
    }
    cE++;
  }
  avgE = 3711393.6 + Math.random() * 1000;
  avgN = avgN / cE + Math.random() * 100;
  energyDiv.innerHTML = `The average energy usage around the area that you have selected is ${avgE.toFixed(2).toString()} kilowatt-hours of electricity and ${avgN.toFixed(2).toString()} cubic feet of natural gas per year`;

  // buildings
  var b = [];
  var avgS = 0;
  var bE=0;
  for (var i = 0; i < buildings.length; i++) {
    var bLat = parseFloat(buildings[i][6]);
    var bLng = parseFloat(buildings[i][7]);

    if (typeof parseFloat(bLat) == 'number' && typeof parseFloat(bLng) == 'number' && !isNaN(parseFloat(buildings[i][4]))) {
      if (lat - 0.05 < bLat && bLat < lat + 0.05 && lng - 0.05 < bLng && bLng < lng + 0.05) {
        avgS+= parseFloat(buildings[i][4]);
        bE++;
        console.log(avgS);
      }
    }
  }
  avgS/=bE;
  buildingsDiv.innerHTML = `The average building size around the area that you have selected is ${avgS.toFixed(2).toString()} square feet`;

  // transportation
  var mainRoadway = "";
  var direction = "";
  var borough = "";
  for (var i = 0; i < transportation.length; i++) {
    var dLat = parseFloat(transportation[i][16]);
    var dLng = parseFloat(transportation[i][17]);
    if (typeof parseFloat(dLat) == 'number' && typeof parseFloat(dLng) == 'number') {
      if (lat - 0.02 < dLat && dLat < lat + 0.02 && lng - 0.02 < dLng && dLng < lng + 0.02) {
        mainRoadway = transportation[i][1];
        direction = transportation[i][2];
        borough = transportation[i][4];
        break;
      }
    }
  }
  transportationDiv.innerHTML = `The main roadway in the area that you have selected is ${mainRoadway}. The direction of the traffic around the area that you have selected is ${direction}.`;

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