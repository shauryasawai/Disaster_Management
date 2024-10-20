import React from "react";

const CalamityResult = ({ isUnderCalamity, disasterType, description }) => {
  return (
    <div
      className="bg-cover bg-center h-screen flex items-center justify-center"
      style={{
        backgroundImage:
          "url('https://www.suredyna.com/wp-content/uploads/2017/10/safety-first-1030x686.jpg.webp')",
      }}
    >
      <div className="flex flex-col items-center p-10 mt-12 rounded-3xl bg-black opacity-60 bg-opacity-60 w-96 text-white">
        <h1 className="text-3xl mb-6">Calamity Result</h1>

        {isUnderCalamity ? (
          <>
            <h2 className="text-2xl mb-4">Warning! Natural Calamity Detected</h2>
            <p>
              <strong>Disaster Type:</strong> {disasterType}
            </p>
            <p>
              <strong>Description:</strong> {description}
            </p>
          </>
        ) : (
          <>
            <h2 className="text-2xl mb-4">This Location is Safe</h2>
            <p>There are currently no known calamities in your area.</p>
          </>
        )}

        <a
          href="http://127.0.0.1:8000/ml/"
          target="_blank"
          className="text-aquamarine mt-6"
        >
          Get Safest Route (Navigation)!!!
        </a>
      </div>
    </div>
  );
};

export default CalamityResult;