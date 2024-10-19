import React from 'react';

const ContactUs = () => {
  return (
    <div className="bg-black text-green-500 min-h-screen">
      <div className="container mx-auto px-4">
        <h1 className="text-center text-3xl font-bold mb-8">Contact Us</h1>
        <form>
          <div className="mb-4">
            <label htmlFor="name" className="block mb-2">Name</label>
            <input
              type="text"
              className="form-control w-full bg-gray-900 text-green-500 border border-green-500 p-2"
              id="name"
              placeholder="Enter your name"
            />
          </div>
          <div className="mb-4">
            <label htmlFor="email" className="block mb-2">Email</label>
            <input
              type="email"
              className="form-control w-full bg-gray-900 text-green-500 border border-green-500 p-2"
              id="email"
              placeholder="Enter your email"
            />
          </div>
          <div className="mb-4">
            <label htmlFor="message" className="block mb-2">Message</label>
            <textarea
              className="form-control w-full bg-gray-900 text-green-500 border border-green-500 p-2"
              id="message"
              rows="4"
              placeholder="Your message"
            ></textarea>
          </div>
          <button type="submit" className="btn bg-green-500 hover:bg-green-400 text-black w-full p-2">
            Submit
          </button>
        </form>
      </div>
      <footer className="text-center py-4 mt-8">
        <p>&copy; 2024 Team Hounds of Justice. All Rights Reserved.</p>
      </footer>
    </div>
  );
};

export default ContactUs;
