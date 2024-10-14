import React from "react";

const CalamityResult = ({ isUnderCalamity, disasterType, description }) => {
  return (
    <div>
      <h1>Calamity Result</h1>
      {isUnderCalamity ? (
        <div>
          <h2>Warning! Natural Calamity Detected</h2>
          <p>
            <strong>Disaster Type:</strong> {disasterType}
          </p>
          <p>
            <strong>Description:</strong> {description}
          </p>
        </div>
      ) : (
        <div>
          <h2>This Location is Safe</h2>
          <p>There are currently no known calamities in your area.</p>
        </div>
      )}
      <a
        href="http://localhost:8888/notebooks/Desktop%2FSmart_India_Hack.ipynb"
        target="_blank"
        rel="noopener noreferrer"
      >
        Get Safest Route (Navigation)!!
      </a>
    </div>
  );
};

export default CalamityResult;
