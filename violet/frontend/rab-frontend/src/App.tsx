import { useState } from 'react'
import { useEffect } from 'react';
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import CameraInput from './components/CameraInput.tsx'
import CaptureBtn from './components/CaptureBtn.tsx'
import Navbar from './components/Navbar.tsx'
import UserAuth from './components/UserAuth/UserAuth.tsx'
import axios from 'axios';

function App() {
  const [count, setCount] = useState(0)

useEffect(() => {
  // This effect runs only once when the App component mounts (because of the empty dependency array [])

  // Send a GET request to the backend at the specified endpoint
  axios.get('http://localhost:3000/api/hello')
    .then(response => {
      // If the request is successful, log the backend's response to the console
      console.log('Backend says:', response.data);
    })
    .catch(error => {
      // If there’s an error (e.g., backend not running), log it for debugging
      console.error('Error contacting backend:', error);
    });

}, []); // ← Empty array means this effect runs once, similar to componentDidMount in class components

  return (
    <>
      <div>

          <UserAuth/>
        {/* <CameraInput />
        <CaptureBtn />
        <Navbar /> */}

      </div>
    </>
  )
}

export default App
