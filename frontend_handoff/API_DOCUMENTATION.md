# Actual API
Base URL: http://127.0.0.1:5000. No authentication is implemented.

|Endpoint|Method|Request|Successful response|
|---|---|---|---|
|/|GET|none|JSON: project="Elaria", status="active", message|
|/health|GET|none|JSON: {"status":"healthy"}|
|/predict|POST|application/json: {"text":"I enjoyed lunch"}|200 JSON: status, record_id, prediction, model_score, disclaimer|
|/predict-csv|POST|multipart/form-data field `file`, filename ending .csv|200 downloadable UTF-8 BOM CSV; filename elaria_predictions.csv|
|/history|GET|none|200 JSON: status, total_records, records|
|/statistics|GET|none|200 JSON: status, total_predictions|

Prediction response schema: `{"status":"success","record_id":<integer>,"prediction":"suicide" or "non-suicide","model_score":<number 0..1>,"disclaimer":<string>}`. Scores always refer to the suicide dataset class, not confidence in the returned label or personal risk. Exact predictions/scores depend on input; no third label exists.
History records contain id, batch_id (nullable), source (single_text/csv), prediction, model_score, created_at. History returns at most 100 newest rows; total_records is the returned count. Statistics counts all stored rows. No delete-history or JSON-array batch route exists.

CSV must be UTF-8 with a `text` column and at least one data row; every text must be a nonempty string. Additional columns are retained. Output adds prediction, model_score and disclaimer; input columns with these reserved names are overwritten. Rows are processed synchronously; all predictions complete before one atomic metadata transaction. No partial-success output.

Errors: 400 JSON {"error":<message>} for missing/invalid JSON or text, absent upload, invalid extension, missing column, empty/malformed CSV and unusable text. Example: {"error":"Please provide non-empty text."}. Requests over 10 MiB return 413 JSON {"error":"File exceeds the maximum upload size of 10 MB."}. Prediction/CSV failures return sanitized 500 JSON; history/statistics SQLite failures return {"error":"Database operation failed."}. Unknown routes and unsupported methods use Flask's default HTML 404/405 responses; callers must inspect content type.
Health confirms the loaded process is running; it is not a live database health probe.
