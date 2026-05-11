function UrlList({ urls, onDelete, baseUrl }) {
  if (urls.length === 0) {
    return <p style={{ color: "#999" }}>Богино URL байхгүй байна.</p>
  }

  return (
    <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 14 }}>
      <thead>
        <tr style={{ borderBottom: "2px solid #ddd", textAlign: "left" }}>
          <th style={{ padding: "8px 4px" }}>Богино URL</th>
          <th style={{ padding: "8px 4px" }}>Анхны URL</th>
          <th style={{ padding: "8px 4px" }}>Дарсан</th>
          <th style={{ padding: "8px 4px" }}>Хугацаа</th>
          <th style={{ padding: "8px 4px" }}></th>
        </tr>
      </thead>
      <tbody>
        {urls.map((url) => (
          <tr key={url.id} style={{ borderBottom: "1px solid #eee" }}>
            <td style={{ padding: "8px 4px" }}>
              <a href={`${baseUrl}/${url.short_code}`} target="_blank" rel="noreferrer">
                {url.short_code}
              </a>
            </td>
            <td style={{ padding: "8px 4px", maxWidth: 200, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
              {url.original_url}
            </td>
            <td style={{ padding: "8px 4px" }}>{url.click_count}</td>
            <td style={{ padding: "8px 4px" }}>
              {url.expires_at ? new Date(url.expires_at).toLocaleDateString() : "—"}
            </td>
            <td style={{ padding: "8px 4px" }}>
              <button onClick={() => onDelete(url.short_code)} style={{ color: "red", background: "none", border: "none", cursor: "pointer" }}>
                Устгах
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}

export default UrlList
