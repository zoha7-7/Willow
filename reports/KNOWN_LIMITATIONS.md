# Known limitations
Approved baseline retains documented negation/context errors; no accuracy improvement or clinical validity is claimed. Labels describe text content.
Windows installation commands are documented but execution was verified on Linux, Python 3.12.14. No frontend/browser CORS integration or internet deployment tested. NLTK data must be installed separately.
CSV predictions are synchronous and row-by-row; 10 MiB bounds input size, not runtime or peak parsing memory. Input result-column names are overwritten. History is limited to 100 newest records. No authentication, retention scheduler, public deletion endpoint or JSON-array batch endpoint.
