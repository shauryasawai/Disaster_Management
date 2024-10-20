import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <div className="flex align-middle justify-center z-20">
      <div className="bg-slate-700 text-white my-9 w-2/3 border-2 border-purple-300 border-spacing-1 rounded-full">
        <ul className="flex justify-around align-middle font-bold text-3xl py-6">
          <Link to="http://127.0.0.1:8000/dashboard/"><li className="list-none hover:cursor-pointer hover:text-green-600">
            Profile
          </li></Link>
          <Link to="http://127.0.0.1:8000/about_us/"><li className="list-none hover:cursor-pointer hover:text-green-600">
            About Us
          </li></Link>
          <Link to="http://127.0.0.1:8000/contact/"><li className="list-none hover:cursor-pointer hover:text-green-600">
            Contact Us
          </li></Link>
          <Link to="http://127.0.0.1:8000/fetch-news/"><li className="list-none hover:cursor-pointer hover:text-green-600">News
          </li></Link>
        </ul>
      </div>
    </div>
  );
};

export default Navbar;
