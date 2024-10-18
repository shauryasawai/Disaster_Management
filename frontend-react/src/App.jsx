import { useState } from "react";
import "./App.css";
import Navbar from "./components/navbar";
import Card from "./components/card";
import Section from "./components/Section";
import Headings from "./components/Headings";
import Panic_button from "./components/Panic_button";
import MapComponent from "./components/MapComponent";
import Footer from "./components/Footer";

function App() {
  return (
    <>
    <div class="video-background">
        <video src="/src/assets/bg_video.mp4" autoPlay muted loop></video>
        
    </div>

    <div class="overlay">
      <Navbar />
      <Panic_button />
      <MapComponent />

      <Headings heading="Contacts" />
      <Section img1="https://tse3.mm.bing.net/th?id=OIP.y15e0sawGcT3ycy4nBpkEwHaHa&pid=Api&P=0&h=180" img2="" img3="https://tse4.mm.bing.net/th?id=OIP.T5tsaslsIK0004CrVJt_wAHaHa&pid=Api&P=0&h=180" img4="https://tse2.mm.bing.net/th?id=OIP.r8MAAiT41rK9WW8O_1jfPwHaHa&pid=Api&P=0&h=180" text1="Fire Rescue" text2="Suwa Seriya" text3="Hospital" text4="Police"/>

      <Headings heading="Services" />
      <Section img1="https://tse1.mm.bing.net/th?id=OIP.jhd3PE403n3R_Ohm9S_noAHaE2&pid=Api&P=0&h=180" img2="" img3="" img4="" text1="Crime Report" text2="Wildlife Conservation" text3="Hazard Alert" text4="Disaster Recovery"/>

      <Headings heading="Information" />
      <Section img1="" img2="" img3="" img4="" text1="Safety Tips" text2="Emergency Preparedness" text3="First Aid Tips" text4="DMC"/>


      <Footer />
      </div>
    </>
  );
}

export default App;
