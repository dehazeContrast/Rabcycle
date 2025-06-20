import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import CameraInput from './components/CameraInput.tsx'
import CaptureBtn from './components/CaptureBtn.tsx'
import Navbar from './components/Navbar.tsx'
import UserAuth from './components/UserAuth/UserAuth.tsx'


function App() {
  const [count, setCount] = useState(0)

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
