import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';  // Import Bootstrap's JS for interactivity

const SliderComponent = () => {
  return (
    <div id="carouselExampleCaptions" className="carousel slide carousel-fade" data-bs-ride="carousel">
      <div className="carousel-indicators">
        <button
          type="button"
          data-bs-target="#carouselExampleCaptions"
          data-bs-slide-to="0"
          className="active"
          aria-current="true"
          aria-label="Slide 1"
        ></button>
        <button
          type="button"
          data-bs-target="#carouselExampleCaptions"
          data-bs-slide-to="1"
          aria-label="Slide 2"
        ></button>
        <button
          type="button"
          data-bs-target="#carouselExampleCaptions"
          data-bs-slide-to="2"
          aria-label="Slide 3"
        ></button>
      </div>
      <div className="carousel-inner">
        <div className="carousel-item active">
          <img
            src="https://static.timesofisrael.com/www/uploads/2023/03/33AN3EN-highres-1024x640.jpg"
            className="d-block w-100"
            alt="Earthquake"
          />
          <div className="carousel-caption d-none d-md-block">
            <h5 style={{ color: 'white' }}>Earthquake</h5>
            <p style={{ color: 'white' }}>
              Some representative placeholder content for the first slide.
            </p>
            <p>
              <a href="#" className="btn btn-danger mt-3">
                Learn More
              </a>
            </p>
          </div>
        </div>
        <div className="carousel-item">
          <img
            src="https://cbsnews1.cbsistatic.com/hub/i/r/2018/08/19/3c6c4bb8-cb45-4e0e-bdbb-28d39d1470d4/thumbnail/1240x834/5d187ee49c6b73f781cedba817130848/ap-18230455383876.jpg"
            className="d-block w-100"
            alt="Flood"
          />
          <div className="carousel-caption d-none d-md-block">
            <h5>Flood</h5>
            <p>Some representative placeholder content for the second slide.</p>
            <p>
              <a href="#" className="btn btn-danger mt-3">
                Learn More
              </a>
            </p>
          </div>
        </div>
        <div className="carousel-item">
          <img
            src="https://cdn.devastatingdisasters.com/wp-content/uploads/2021/08/1-fires.jpg"
            className="d-block w-100"
            alt="Fire"
          />
          <div className="carousel-caption d-none d-md-block">
            <h5 style={{ color: 'white' }}>Fire</h5>
            <p style={{ color: 'white' }}>
              Some representative placeholder content for the third slide.
            </p>
            <p>
              <a href="#" className="btn btn-danger mt-3">
                Learn More
              </a>
            </p>
          </div>
        </div>
      </div>
      <button
        className="carousel-control-prev"
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide="prev"
      >
        <span className="carousel-control-prev-icon" aria-hidden="true"></span>
        <span className="visually-hidden">Previous</span>
      </button>
      <button
        className="carousel-control-next"
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide="next"
      >
        <span className="carousel-control-next-icon" aria-hidden="true"></span>
        <span className="visually-hidden">Next</span>
      </button>
    </div>
  );
};

export default SliderComponent;
