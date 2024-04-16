let map;
let directionsService;
let directionsRenderer;

function initMap() {
    const userLocation = { lat: 41.9266713, lng: -88.1236418 };
    map = new google.maps.Map(document.getElementById("map"), {
      zoom: 14,
      center: userLocation,
    });

    directionsService = new google.maps.DirectionsService();
    directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);

    calculateAndDisplayRoute(directionsService, directionsRenderer, userLocation);
}

function calculateAndDisplayRoute(directionsService, directionsRenderer, userLocation) {
    const request = {
      origin: userLocation,
      destination: { lat: 41.93227340669935, lng: -88.07939870317989 }, // Replace with actual destination coordinates
      travelMode: 'DRIVING',
      // Add other parameters if needed
    };

    directionsService.route(request, (result, status) => {
      if (status === 'OK') {
        directionsRenderer.setDirections(result);
      } else {
        window.alert('Directions request failed due to ' + status);
      }
    });
}