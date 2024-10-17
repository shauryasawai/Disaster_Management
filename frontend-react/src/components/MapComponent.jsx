import React, { useEffect, useState } from "react";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import $ from "jquery";

const MapComponent = () => {
  const [latitude, setLatitude] = useState(null);
  const [longitude, setLongitude] = useState(null);
  const [city, setCity] = useState("Not available");
  const [state, setState] = useState("Not available");

  // Get user's location on component mount
  useEffect(() => {
    getLocation();
  }, []);

  // Function to get location using browser's geolocation
  const getLocation = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showMap, showError);
    } else {
      alert("Geolocation is not supported by this browser.");
    }
  };

  // Function to display map and location data
  const showMap = (position) => {
    const lat = position.coords.latitude;
    const lng = position.coords.longitude;
    setLatitude(lat);
    setLongitude(lng);

    // Initialize map
    const map = L.map("map").setView([lat, lng], 13);
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 18,
      attribution: "© OpenStreetMap",
    }).addTo(map);

    // Add marker
    const marker = L.marker([lat, lng]).addTo(map);
    marker.bindPopup("<b>Your Location</b><br>Lat: " + lat + "<br>Lon: " + lng).openPopup();

    // Get city and state
    getCityState(lat, lng);
  };

  // Function to get city and state based on coordinates
  const getCityState = (lat, lng) => {
    const url = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}&zoom=10&addressdetails=1`;

    $.getJSON(url, (data) => {
      const city = data.address.city || data.address.town || data.address.village || "Unknown City";
      const state = data.address.state || "Unknown State";
      setCity(city);
      setState(state);
    }).fail(() => {
      setCity("Unable to retrieve city");
      setState("Unable to retrieve state");
    });
  };

  // Error handler for geolocation
  const showError = (error) => {
    switch (error.code) {
      case error.PERMISSION_DENIED:
        alert("User denied the request for Geolocation.");
        break;
      case error.POSITION_UNAVAILABLE:
        alert("Location information is unavailable.");
        break;
      case error.TIMEOUT:
        alert("The request to get user location timed out.");
        break;
      default:
        alert("An unknown error occurred.");
    }
  };

  return (
    <div data-bs-theme="dark" className="my-60">
      {/* Coordinates Section */}
      <section id="coordinates" style={{ textAlign: "center", margin: "15px 0" }}>
        <h1 className="text-4xl">Your Coordinates</h1>
        <p>Latitude: {latitude ? latitude : "Not available"}, Longitude: {longitude ? longitude : "Not available"}</p>
        <p>City: {city}, State: {state}</p>
      </section>

      {/* Map Section */}
      <section id="location-section" className="flex justify-center items-center">
        <div id="map" style={{ height: "700px", width: "80%" }}></div>
      </section>
    </div>
  );
};

export default MapComponent;