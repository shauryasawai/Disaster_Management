import React from "react";

const Panic_button = () => {
  return (
      <div className="flex justify-center items-center">
        <a href="http://127.0.0.1:8000/check_disaster/"><button className="bg-red-600 border rounded-md py-6 px-6 text-2xl font-bold text-wrap mx-auto">
          <h1>PANIC Button</h1>
        </button></a>
      </div>
  );
};

export default Panic_button;
