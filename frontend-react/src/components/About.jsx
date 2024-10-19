import React from 'react';

const AboutUs = () => {
  return (
    <div className="bg-gray-900 text-gray-200">
      {/* Hero Section */}
      <section className="bg-green-800 text-white py-12 text-center">
        <div className="container mx-auto">
          <h1 className="text-4xl font-bold">About Us</h1>
          <p className="mt-4">Learn more about the Disaster Management Web App</p>
        </div>
      </section>

      {/* Content Section */}
      <section className="py-12">
        <div className="container mx-auto px-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div>
              <h2 className="text-green-500 text-2xl font-bold">Overview</h2>
              <p className="mt-4">
                The Disaster Management Web App is designed to provide real-time assistance during natural disasters by integrating data from various sources, including the OCHA (United Nations Office for the Coordination of Humanitarian Affairs) database and satellite imagery.
              </p>
            </div>
            <div>
              <img src="https://via.placeholder.com/500" alt="Disaster Management" className="rounded-lg" />
            </div>
          </div>

          <hr className="border-green-500 my-8" />

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
            <div>
              <i className="fas fa-map-marker-alt text-green-500 text-4xl"></i>
              <h3 className="text-green-500 text-xl font-bold mt-4">Location Tracking</h3>
              <p className="mt-2">Automatically fetches and displays the user's current GPS coordinates on an interactive map.</p>
            </div>
            <div>
              <i className="fas fa-broadcast-tower text-green-500 text-4xl"></i>
              <h3 className="text-green-500 text-xl font-bold mt-4">Disaster Monitoring</h3>
              <p className="mt-2">Cross-references location data with the OCHA database to detect ongoing disasters and provide critical information.</p>
            </div>
            <div>
              <i className="fas fa-route text-green-500 text-4xl"></i>
              <h3 className="text-green-500 text-xl font-bold mt-4">Safe Routes & Navigation</h3>
              <p className="mt-2">Displays the safest evacuation routes based on satellite imagery and predefined safe zones.</p>
            </div>
          </div>

          <hr className="border-green-500 my-8" />

          <div>
            <h2 className="text-center text-green-500 text-2xl font-bold">Key Features</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mt-8">
              <div>
                <h4 className="text-xl font-bold">Real-time Location Tracking</h4>
                <p className="mt-2">Your location is pinpointed using GPS coordinates, which are updated in real-time.</p>
              </div>
              <div>
                <h4 className="text-xl font-bold">Disaster Detection & Monitoring</h4>
                <p className="mt-2">Cross-reference your location with the OCHA database to detect any ongoing calamities.</p>
              </div>
              <div>
                <h4 className="text-xl font-bold">Emergency Guidelines & Navigation</h4>
                <p className="mt-2">Get the safest routes for evacuation, safety protocols, and other emergency information based on real-time data.</p>
              </div>
              <div>
                <h4 className="text-xl font-bold">Emergency Assistance</h4>
                <p className="mt-2">Access nearby emergency shelters, medical assistance, and necessary survival tips all in one place.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-green-800 text-center py-4">
        <p>&copy; 2024 Disaster Management Web App. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default AboutUs;