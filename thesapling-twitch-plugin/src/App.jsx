import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  const baseURL = "https://wndrls58i9.execute-api.eu-west-3.amazonaws.com/dev/camera-path-proposals"

  const handleClick = () => {

    fetch(baseURL, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ path: 'test' }),
    }).then((response) => response.json()).then((data) => console.log(data))
      .catch((error) => {
        console.error('Error:', error)
      })
  }

  return (
    <>
      <h1>Wessel is de beste</h1>
      <button onClick={handleClick}>Click me</button>
    </>
  )
}

export default App
