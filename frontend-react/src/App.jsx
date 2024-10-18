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
    <div class="video-background">
        <video src="https://s2.ezgif.com/tmp/ezgif-2-534c969211.mp4" autoPlay muted loop></video>
        
    </div>

    <div class="overlay">

    
      <Navbar />
      <Panic_button />
      <Headings heading="Contacts" />
      <Section bg="https://static.vecteezy.com/system/resources/previews/046/030/063/mp4/4k-purple-dust-and-bokeh-particles-animation-background-video.mp4" img1="https://tse3.mm.bing.net/th?id=OIP.y15e0sawGcT3ycy4nBpkEwHaHa&pid=Api&P=0&h=180" img2="" img3="https://tse4.mm.bing.net/th?id=OIP.T5tsaslsIK0004CrVJt_wAHaHa&pid=Api&P=0&h=180" img4="https://tse2.mm.bing.net/th?id=OIP.r8MAAiT41rK9WW8O_1jfPwHaHa&pid=Api&P=0&h=180" text1="Fire Rescue" text2="Suwa Seriya" text3="Hospital" text4="Police"/>
      <Headings heading="Services" />
      <Section bg="https://static.vecteezy.com/system/resources/previews/046/030/039/mp4/4k-sci-fi-tunnel-warp-motion-background-video.mp4" img1="" img2="" img3="" img4="" text1="Crime Report" text2="Wildlife Conservation" text3="Hazard Alert" text4="Disaster Recovery"/>
      <Headings heading="Information" />
      <Section bg="https://static.vecteezy.com/system/resources/previews/046/030/036/mp4/4k-starry-tunnel-motion-background-video.mp4" img1="" img2="" img3="" img4="" text1="Safety Tips" text2="Emergency Preparedness" text3="First Aid Tips" text4="DMC"/>

      </div>
    </>
  );
}

export default App;
