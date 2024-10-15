import { useState } from "react";
import "./App.css";
import Navbar from "./components/navbar";
import Card from "./components/card";
import Section from "./components/Section";
import Headings from "./components/Headings";

function App() {
  return (
    <>
      <Navbar />
      <Headings heading="Contacts" />
      <Section />
      <Headings heading="Services" />
      <Section />
      <Headings heading="Information" />
      <Section />
    </>
  );
}

export default App;
