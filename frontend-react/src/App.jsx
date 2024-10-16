import { useState } from "react";
import "./App.css";
import Navbar from "./components/navbar";
import Card from "./components/card";
import Section from "./components/Section";
import Headings from "./components/Headings";
import Panic_button from "./components/Panic_button";

function App() {
  return (
    <>
      <Navbar />
      <Panic_button />
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
