# Willow – Member 5 frontend

This is a React + Vite frontend based on the Willow reference screenshot. It includes:
- Willow landing page with an animated illustrated hero and an Enter Willow link to the interface
- Text prediction form
- CSV bulk prediction (one API request per non-empty row)
- Downloadable prediction CSV
- Latest prediction and session history
- Responsible Use and supportive daily thought
- Responsive layout and light/dark theme toggle

The landing page opens first. Select **Enter Willow** to use the prediction interface; use the home button in the interface header to return to the landing page.

## 1. Start the frontend

Open PowerShell in this `willow_member5_code` folder. If PowerShell starts in the workspace root, first run `cd .\willow_member5_code`.

```powershell
npm install
npm run dev
```

Open the URL Vite prints (normally `http://localhost:8080`).

Run the interface checks and production build with:

```powershell
npm test
npm run build
```

## 2. Connect the Flask backend

The frontend expects this endpoint:

**POST** `/api/predict`

Request:
```json
{"text": "text to classify"}
```

Response:
```json
{
  "prediction": "Suicide",
  "confidence": 0.53,
  "model_prediction": "Non-suicide",
  "prediction_source": "explicit_language"
}
```

Only `prediction` is required. `confidence`, `model_prediction`, and `prediction_source` are optional; `prediction_source` may be `explicit_language` when the backend applies an explicit-language flag. The interface displays both the flagged result and underlying model label in that case, and includes the model label/source in downloaded CSVs. Vite proxies `/api` to `http://127.0.0.1:5000`.

## 3. Connect your existing model files

Start the Flask backend in a second terminal; the frontend alone cannot make model predictions. The backend must listen on `127.0.0.1:5000` and provide `POST /api/predict`. The frontend does not load model files directly.

`BACKEND_INTEGRATION_EXAMPLE.py` is only a route contract example. No Flask app, model handler, or trained model artifacts are included in this folder, so connect your actual backend and its new model there rather than guessing a prediction function here.

## 4. CSV format

CSV must have a header row. A text-like header such as `text`, `post`, `thought`, `content`, or `message` is selected automatically when possible. You can change the text column after upload. Every non-empty row is sent to `/api/predict`; results are appended as `Willow_Prediction`, `Willow_Model_Prediction`, `Willow_Prediction_Source`, and `Willow_Confidence`.

For large CSV files, consider implementing a batch endpoint in Flask rather than sending one request per row.

## 5. Important safety note

This is an educational classification interface, not a clinical screening or diagnostic tool. Model output can be wrong and must not be used as the sole basis for assessing anyone's safety. If someone may be in immediate danger, contact emergency services or a trusted person. In India, emergency assistance is available at 112; Tele-MANAS can be reached at 14416.
