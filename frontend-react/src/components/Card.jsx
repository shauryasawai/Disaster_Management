import React from "react";

const Card = ({img, text}) => {
  return (
    <div className="bg-black h-40 w-40 text-white my-9 border-2 border-purple-300 border-spacing-1 rounded-2xl">
      <img
        className="h-40 w-40 border-2 rounded-2xl"
        src={img}
        alt=""
      />
      <div className="flex justify-center items-center">
        <p className="text-black">{text}</p>
      </div>
    </div>
  );
};

export default Card;
