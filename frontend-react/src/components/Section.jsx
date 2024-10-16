import React from "react";
import Card from "./card";

const Section = () => {
  return (
    <div className="flex justify-center items-center my-2">
      <div className="bg-white h-60 w-[90%] text-white border-2 border-purple-300 border-spacing-1 rounded-10 flex justify-around items-center rounded-2xl">
        <Card />
        <Card />
        <Card />
        <Card />
      </div>
    </div>
  );
};

export default Section;
