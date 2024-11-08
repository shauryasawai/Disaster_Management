import React from "react";

const Card = ({ img, text }) => {
  return (
    <div className="bg-orange text-white my-6 rounded-2xl">
      <img
        className="w-24 h-24 sm:w-32 sm:h-32 md:w-36 md:h-36 lg:w-40 lg:h-40 border-2 border-purple-300 rounded-2xl mx-auto"
        src={img}
        alt={text}
      />
      <div className="flex justify-center items-center mt-2">
        <p className="text-sm sm:text-base md:text-lg lg:text-xl font-bold text-center">{text}</p>
      </div>
    </div>
  );
};

export default Card;