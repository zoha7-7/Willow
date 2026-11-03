# Actual verification

Linux Python 3.12.14; actual Flask HTTP server, temporary SQLite database, synthetic inputs only.

- PASS: Flask startup and health over HTTP
- PASS: Home endpoint
- PASS: Single text: 1
- PASS: Single text: 2
- PASS: Both binary classes
- PASS: Invalid JSON input {}
- PASS: Invalid JSON input {'text': ''}
- PASS: Invalid JSON input {'text': 42}
- PASS: Invalid JSON input {'text': '123 !!!'}
- PASS: Invalid JSON input []
- PASS: Invalid JSON input {'text': '   '}
- PASS: Malformed JSON
- PASS: CSV output, original columns and single/batch consistency
- PASS: CSV missing column
- PASS: CSV empty
- PASS: CSV header only
- PASS: CSV malformed
- PASS: CSV missing value
- PASS: Invalid extension
- PASS: Missing upload
- PASS: Oversized request
- PASS: History and metadata privacy
- PASS: Statistics
- PASS: Atomic rollback
- PASS: Approved candidate dimensions
- PASS: Preprocessing preserves contraction negation
- PASS: Direct/HTTP consistency
- PASS: Database failure sanitized
- PASS: Documented python -m BACKEND.app startup on port 5000

Total: 29 checks passed. No held-out data, training, or historical GA tests used. Dependencies verified against candidate manifest. Missing NLTK resources installed; no Python package upgrades.
