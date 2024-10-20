import React from "react";
import Card from "./card";

const Section = ({link1, link2, link3, link4, bg, img1, img2, img3, img4, text1, text2, text3, text4}) => {
  return (
    <div className="relative flex justify-center items-center my-6 ">
      <div className="h-80 w-[90%] relative z-10 text-white border-2 bg-black border-purple-300 border-spacing-1 rounded-10 flex justify-around items-center rounded-2xl">
        <a href={link1}><Card img={img1} text={text1}/></a>
        <a href={link2}><Card img={img2} text={text2}/></a>
        <a href={link3}><Card img={img3} text={text3}/></a>
        <a href={link4}><Card img={img4} text={text4}/></a>
      </div>
    </div>
  );
};

export default Section;
