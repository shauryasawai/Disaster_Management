import React from "react";

const MovingColorfulBorder = () => {
  return (
    <div className="flex items-center justify-center h-screen bg-gray-100">
      <div className="relative w-52 h-52 flex items-center justify-center">
        <div className="absolute top-[-5px] left-[-5px] right-[-5px] bottom-[-5px] bg-gradient-to-r from-red-500 via-yellow-500 via-green-500 via-blue-500 to-purple-500 animate-moving-border bg-[length:300%_300%] z-[-1]" />
        <div className="w-full h-full bg-white flex items-center justify-center relative z-[1]">
          <p className="text-center text-lg">Content Here</p>
        </div>
      </div>
    </div>
  );
};

export default MovingColorfulBorder;
