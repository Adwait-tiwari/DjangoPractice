import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [message,setMessage] =useState(' ')
  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/home")
      .then((res) => res.json())
      .then((data)=>setMessage(data.message))
      .catch((err)=> console.log("Error is occouring",err))
  }, [])
  
  return (
    <div style={{ textAlign: "center", marginTop: "40px" }}>
      <h1>Django + React Integration</h1>
      <h2>{message}</h2>
    </div>
  )
}

export default App
