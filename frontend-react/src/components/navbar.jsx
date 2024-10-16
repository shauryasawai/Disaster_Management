import React from "react";

const Navbar = () => {
  return (
    <div className="flex align-middle justify-center z-20">
      <div className="bg-black text-white my-9 w-2/3 border-2 border-purple-300 border-spacing-1 rounded-full">
        <ul className="flex justify-around align-middle font-bold text-3xl py-6">
          <li className="list-none hover:cursor-pointer hover:text-green-600">
            Home
          </li>
          <li className="list-none hover:cursor-pointer hover:text-green-600">
            About
          </li>
          <li className="list-none hover:cursor-pointer hover:text-green-600">
            Contact Us
          </li>
          <li className="list-none hover:cursor-pointer hover:text-green-600">
            News
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Navbar;
