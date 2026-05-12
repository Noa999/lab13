import { useState } from "react"

function ShortenForm({ onShorten }) {
  const [url, setUrl] = useState("")
  const [expiresAt, setExpiresAt] = useState("")
  const [error, setError] = useState("")

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError("")
    if (!url) {
      setError("URL оруулна уу")
      return
    }
    try {
      await onShorten(url, expiresAt || null)
      setUrl("")
      setExpiresAt("")
    } catch {
      setError("Алдаа гарлаа")
    }
  }

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: 32 }}>
      <div style={{ display: "flex", gap: 8, marginBottom: 8 }}>
        <input
          type="url"
          placeholder="https://example.com/long-url"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          style={{ flex: 1, padding: "8px 12px", fontSize: 15 }}
        />
        <button type="submit" style={{ padding: "8px 20px" }}>
          Богиносгох
        </button>
      </div>
      <div>
        <label style={{ fontSize: 13, color: "#666" }}>
          Хугацаа дуусах (заавал биш):&nbsp;
          <input
            type="datetime-local"
            value={expiresAt}
            onChange={(e) => setExpiresAt(e.target.value)}
          />
        </label>
      </div>
      {error && <p style={{ color: "red", margin: "4px 0" }}>{error}</p>}
    </form>
  )
}

export default ShortenForm
