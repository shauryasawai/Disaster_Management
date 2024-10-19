import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { createBrowserRouter,RouterProvider } from "react-router-dom";
import About from './components/About.jsx';
import Contact_Us from './components/Contact_Us.jsx';
import News from './components/News.jsx';
import CalamityResult from './components/calamity_result.jsx';

const router = createBrowserRouter([
  {
    path:"/",
    element:<App/>
  },
  {
    path: "/about",
    element: <About/>
  },
  {
    path: "/contactus",
    element: <Contact_Us/>
  },
  {
    path: "/news",
    element: <News/>
  },
  {
    path:"/calamityresult",
    element: <CalamityResult/>
  }
])
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router}>
      <App />
    </RouterProvider>
  </StrictMode>,
)
