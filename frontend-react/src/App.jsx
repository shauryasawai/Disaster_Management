import "./App.css";
import Navbar from "./components/navbar";
import Section from "./components/Section";
import Headings from "./components/Headings";
import Panic_button from "./components/Panic_button";
import MapComponent from "./components/MapComponent";
import Footer from "./components/Footer";
import SliderComponent from "./components/SliderComponent";

function App() {
  return (
    <>
      <div class="video-background">
        <video src="https://cdn.pixabay.com/video/2023/04/09/158166-816075064_large.mp4" autoPlay muted loop></video>
      </div>

      <div class="overlay">
        <Navbar />
        <SliderComponent />

        <MapComponent />
        <Panic_button />

        <Headings heading="Contacts" />
        <Section
        link1="http://127.0.0.1:8000/fire_safety/"
        link2="http://127.0.0.1:8000/fetch-news/"
        link3="http://127.0.0.1:8000/hospital/"
        link4="http://127.0.0.1:8000/report/"
          img1="https://tse3.mm.bing.net/th?id=OIP.y15e0sawGcT3ycy4nBpkEwHaHa&pid=Api&P=0&h=180"
          img2="https://tse2.mm.bing.net/th?id=OIP.EjAL2jn03BXr8OOlqUFm7gHaEK&pid=Api&P=0&h=180"
          img3="https://tse4.mm.bing.net/th?id=OIP.T5tsaslsIK0004CrVJt_wAHaHa&pid=Api&P=0&h=180"
          img4="https://tse2.mm.bing.net/th?id=OIP.r8MAAiT41rK9WW8O_1jfPwHaHa&pid=Api&P=0&h=180"
          text1="Fire Rescue"
          text2="NEWS"
          text3="Hospital"
          text4="Police"
        />

        <Headings heading="Services" />
        <Section
        link1="http://127.0.0.1:8000/report-crime/"
        link2="http://127.0.0.1:8000/wildlife/"
        link3="http://127.0.0.1:8000/hazard/"
        link4="http://127.0.0.1:8000/disaster_recovery/"
          img1="https://tse1.mm.bing.net/th?id=OIP.jhd3PE403n3R_Ohm9S_noAHaE2&pid=Api&P=0&h=180"
          img2="https://tse1.mm.bing.net/th?id=OIP.I7zYkFxUQLSBelgIhcTsPwHaEo&pid=Api&P=0&h=180"
          img3="https://tse2.mm.bing.net/th?id=OIP.9wauuU56-IpVuHYd0gJ2XwHaHa&pid=Api&P=0&h=180"
          img4="https://tse2.mm.bing.net/th?id=OIP.q47jLgUA-CgX6JhDfK6wGgHaEc&pid=Api&P=0&h=180"
          text1="Crime Report"
          text2="Wildlife Conservation"
          text3="Hazard Alert"
          text4="Disaster Recovery"
        />

        <Headings heading="Information" />
        <Section
        link1="http://127.0.0.1:8000/first_aid_tips/"
        link2="http://127.0.0.1:8000/emergency/"
        link3="http://127.0.0.1:8000/aid/"
        link4="http://127.0.0.1:8000/ndrf/"
          img1="https://tse2.mm.bing.net/th?id=OIP.gMF4-ClF1h6m2oy0mK6B-wHaHZ&pid=Api&P=0&h=180"
          img2="https://tse2.mm.bing.net/th?id=OIP.CQ90nXRWgXRem7MZCTwFsAHaHa&pid=Api&P=0&h=180"
          img3="https://tse4.mm.bing.net/th?id=OIP.nwloEt0OKLLll4Vzk8EN9gHaE8&pid=Api&P=0&h=180"
          img4="https://tse1.mm.bing.net/th?id=OIP.SjVhEayinC8XcRIBOzCT2wHaEK&pid=Api&P=0&h=180"
          text1="Safety Tips"
          text2="Emergency Preparedness"
          text3="First Aid Tips"
          text4="NDRF"
        />

        <Footer />
      </div>
    </>
  );
}

export default App;
