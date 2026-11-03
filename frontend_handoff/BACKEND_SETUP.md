# Setup (Windows PowerShell)
Use Python 3.12 (verified here: 3.12.14). From the extracted ELARIA_FINAL_HANDOFF directory:
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m nltk.downloader punkt_tab stopwords wordnet
$env:ELARIA_DATABASE_PATH = Join-Path $PWD 'local_test.db'
.\.venv\Scripts\python.exe -m BACKEND.app
```
Keep this terminal open. Server: http://127.0.0.1:5000. Ctrl+C stops it. Debug mode is disabled. Default SQLite path, if unset: BACKEND/database/elaria.db. No existing database is shipped.
On Linux use `python3.12 -m venv .venv`, then `.venv/bin/python` in place of the PowerShell executable above.
Installation needs internet for Python wheels and NLTK resources. No resources download at application startup. Missing/corrupt artifacts or incompatible dependency versions fail startup; do not mix models/vectorizers from different candidates.

## Personal testing (second PowerShell terminal)
```powershell
Invoke-RestMethod http://127.0.0.1:5000/health
$body = @{text='I enjoyed lunch with friends'} | ConvertTo-Json
Invoke-RestMethod http://127.0.0.1:5000/predict -Method Post -ContentType 'application/json' -Body $body
@('Your first sentence','Your second sentence') | ForEach-Object {
  Invoke-RestMethod http://127.0.0.1:5000/predict -Method Post -ContentType 'application/json' -Body (@{text=$_} | ConvertTo-Json)
}
@([pscustomobject]@{id=1;text='I enjoyed lunch with friends'}) | Export-Csv .\test.csv -NoTypeInformation -Encoding UTF8
curl.exe -f -F "file=@test.csv" http://127.0.0.1:5000/predict-csv -o predictions.csv
Invoke-RestMethod http://127.0.0.1:5000/history
Invoke-RestMethod http://127.0.0.1:5000/statistics
.\.venv\Scripts\python.exe -B tests/verify_backend.py
```
The verification script starts its own temporary loopback server and database; it does not use your local_test.db.

## Privacy and test-record removal
The database stores ID, batch ID, source, binary prediction, score and UTC timestamp; not submitted or cleaned text. Application errors log exception types, not input bodies. CSV download includes original input columns, including your text; keep that file private. HTTP access logs contain request paths/status, not request bodies. Other infrastructure may log separately.
To clear only your dedicated local test database, stop the server, then run:
```powershell
.\.venv\Scripts\python.exe -c "import sqlite3; c=sqlite3.connect('local_test.db'); c.execute('DELETE FROM predictions'); c.commit(); c.close()"
```
This deliberately deletes all prediction records in local_test.db; never point it at a database you need to preserve.
