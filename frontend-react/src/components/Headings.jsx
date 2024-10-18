import React from 'react'

const Headings = ({heading}) => {
  return (
    <div className='w-full h-32 font-bold text-6xl text-green-600 flex justify-center items-end'>
      <h1>{heading}</h1>
    </div>
  )
}

export default Headings
