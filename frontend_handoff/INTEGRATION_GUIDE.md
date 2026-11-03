# Frontend integration
Prefer a same-origin reverse proxy. CORS is not enabled; a frontend on another port/origin cannot assume browser access. Add an explicit allowed-origin policy during frontend integration if separate origins are required; do not disable browser security. No frontend integration was performed or tested.

Text:
```javascript
const response = await fetch('/predict', {
  method: 'POST', headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({text: inputText})
});
const result = await response.json();
if (!response.ok) throw new Error(result.error || 'Prediction failed');
// Display result.prediction and result.disclaimer.
// If displaying model_score, label it probability for the suicide content class.
```
CSV:
```javascript
const form = new FormData(); form.append('file', selectedFile);
const response = await fetch('/predict-csv', {method: 'POST', body: form});
if (!response.ok) throw new Error((await response.json()).error);
const csvBlob = await response.blob(); // Offer a download; revoke object URLs afterwards.
```
Do not set multipart Content-Type yourself. Enforce the 10 MiB request limit and .csv/text-column requirements before upload; handle server validation errors too. There is no public JSON batch endpoint: use individual calls or CSV. Fetch /history and /statistics as JSON. Avoid exposing submitted text in client telemetry.
Only two prediction labels: suicide and non-suicide. Never interpret a negative result as assurance of safety. Negation/context failures remain. There is no authentication/rate limiting; do not expose this development server publicly. Hosting, TLS, access control and CORS policy require deployment work.
