import { useState, useEffect } from "react"
import ShortenForm from "./components/ShortenForm"
import UrlList from "./components/UrlList"

const API = "http://localhost:8000"

function App() {
  const [urls, setUrls] = useState([])

  const fetchUrls = async () => {
    const res = await fetch(`${API}/api/v1/urls`)
    const data = await res.json()
    setUrls(data)
  }

  useEffect(() => {
    fetchUrls()
  }, [])

  const handleShorten = async (originalUrl, expiresAt) => {
    const body = { original_url: originalUrl }
    if (expiresAt) body.expires_at = expiresAt
    const res = await fetch(`${API}/api/v1/shorten`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    })
    if (res.ok) {
      fetchUrls()
    }
  }

  const handleDelete = async (shortCode) => {
    await fetch(`${API}/api/v1/urls/${shortCode}`, { method: "DELETE" })
    fetchUrls()
  }

  return (
    <div style={{ maxWidth: 700, margin: "40px auto", padding: "0 20px" }}>
      <h1>URL Shortener</h1>
      <ShortenForm onShorten={handleShorten} />
      <UrlList urls={urls} onDelete={handleDelete} baseUrl={API} />
    </div>
  )
}

export default App
