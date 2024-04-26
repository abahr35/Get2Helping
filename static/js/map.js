let map;
let directionsService;
let directionsRenderer;
let destinationMarker; // Marker for the destination
let currentRoute = {}; // Initialize currentRoute at a higher scope to ensure it's accessible
let marker;

function initMap() {
    const defaultLocation = userLocation; // Ensure this is correctly defined

    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 8,
        center: defaultLocation
    });

    marker = new google.maps.Marker({
        position: defaultLocation,
        map: map,
        title: 'User Location'
    });

    directionsService = new google.maps.DirectionsService();
    directionsRenderer = new google.maps.DirectionsRenderer({
        map: map // Make sure to set the map for the renderer
    });
}

function updateLocation(newLat, newLng) {
    const newPosition = { lat: newLat, lng: newLng };
    map.setCenter(newPosition);
    marker.setPosition(newPosition);
}

function updateDestination(lat, lng, title) {
    const newDestination = { lat, lng };

    // Remove the existing marker if it exists
    if (destinationMarker) {
        destinationMarker.setMap(null);
    }

    // Place a new marker at the destination
    destinationMarker = new google.maps.Marker({
        position: newDestination,
        map: map,
        title: title
    });

    // Update the current route destination
    currentRoute.destination = newDestination;

    // Update the route on the map
    calculateAndDisplayRoute(userLocation, currentRoute.destination);

    // Center the map on the new destination
    map.setCenter(newDestination);
}

function calculateAndDisplayRoute(origin, destination) {
    const request = {
        origin: origin,
        destination: destination,
        travelMode: 'DRIVING'
    };

    directionsService.route(request, (result, status) => {
        if (status === 'OK') {
            directionsRenderer.setDirections(result);
        } else {
            console.error('Directions request failed due to ' + status);
        }
    });
}
