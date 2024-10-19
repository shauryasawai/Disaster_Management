import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <div className="flex align-middle justify-center z-20">
      <div className="bg-slate-700 text-white my-9 w-2/3 border-2 border-purple-300 border-spacing-1 rounded-full">
        <ul className="flex justify-around align-middle font-bold text-3xl py-6">
          <a href="/"><li className="list-none hover:cursor-pointer hover:text-green-600">
            Home
          </li></a>
<<<<<<< HEAD
          <a href="http://127.0.0.1:5501/base/Templates/base/about_us.html"><li className="list-none hover:cursor-pointer hover:text-green-600">
=======
          <a href="http://127.0.0.1:3000/base/Templates/base/about_us.html"><li className="list-none hover:cursor-pointer hover:text-green-600">
>>>>>>> 5709be600a5791d2ad78e8b438a74d5d5fbcce8b
            About Us
          </li></a>
          <a href="http://127.0.0.1:5501/base/Templates/base/contact_us.html"><li className="list-none hover:cursor-pointer hover:text-green-600">
            Contact Us
          </li></a>
          <a href="http://127.0.0.1:5501/base/Templates/base/news.html"><li className="list-none hover:cursor-pointer hover:text-green-600">
            News
          </li></a>
        </ul>
      </div>
    </div>
  );
};

export default Navbar;
