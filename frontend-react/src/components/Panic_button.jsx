import React from "react";
import { Link } from "react-router-dom";

const Panic_button = () => {
  return (
      <div className="flex justify-center items-center">
        <Link to="/calamityresult"><button className="bg-red-600 border rounded-md py-6 px-6 text-2xl font-bold text-wrap mx-auto">
          <h1>PANIC Button</h1>
        </button></Link>
      </div>
  );
};

export default Panic_button;
