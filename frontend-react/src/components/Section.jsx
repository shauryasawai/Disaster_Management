import React from 'react'
import Card from './card'

const Section = () => {
  return (
    <div className='bg-white h-80 w-[90%] text-white my-9 border-2 border-purple-300 border-spacing-1 rounded-10 flex justify-around items-center'>
      <Card />
      <Card />
      <Card />
      <Card />
    </div>
  )
}

export default Section
