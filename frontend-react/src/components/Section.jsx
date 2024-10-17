import React from "react";
import Card from "./card";

const Section = ({bg, img1, img2, img3, img4, text1, text2, text3, text4}) => {
  return (
    <div className="flex justify-center items-center my-2">
      <div className="bg-white h-60 w-[90%] text-white border-2 border-purple-300 border-spacing-1 rounded-10 flex justify-around items-center rounded-2xl">
        <Card img={img1} text={text1}/>
        <Card img={img2} text={text2}/>
        <Card img={img3} text={text3}/>
        <Card img={img4} text={text4}/>
      </div>
    </div>
  );
};

export default Section;
