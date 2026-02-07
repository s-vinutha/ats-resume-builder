export async function generateResume(data) {
  const response = await fetch("http://127.0.0.1:5000/generate-resume", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  return response.json();
}

export async function getATSScore(data) {
  const response = await fetch("http://127.0.0.1:5000/ats-score", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  return response.json();
}
