"""Approved corrected binary candidate; no GA or legacy fallback."""
from pathlib import Path
import hashlib, json, importlib.util
from importlib.metadata import version
import joblib
ROOT=Path(__file__).resolve().parents[1]
CANDIDATE=ROOT/'candidates'/'negation_xgb'
manifest=json.loads((CANDIDATE/'artifact_manifest.json').read_text())
for name,digest in manifest['sha256'].items():
    path=CANDIDATE/name
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
        raise RuntimeError('Missing or incompatible candidate artifact: '+name)
for name,expected in manifest['versions'].items():
    if name!='python' and version(name)!=expected:
        raise RuntimeError('Candidate dependency version mismatch: '+name+'; install requirements.txt')
spec=importlib.util.spec_from_file_location('elaria_candidate_preprocessing',CANDIDATE/'preprocessing.py')
preprocessing=importlib.util.module_from_spec(spec)
spec.loader.exec_module(preprocessing)
clean_text=preprocessing.clean_text
model=joblib.load(CANDIDATE/'model.pkl')
vectorizer=joblib.load(CANDIDATE/'vectorizer.pkl')
label_to_number=joblib.load(CANDIDATE/'label_mapping.pkl')
if label_to_number!={'non-suicide':0,'suicide':1}:
    raise RuntimeError('Incompatible label mapping')
if model.n_features_in_!=len(vectorizer.get_feature_names_out()) or model.n_features_in_!=5000:
    raise RuntimeError('Model/vectorizer feature dimensions disagree')
if set(model.classes_)!={0,1}:raise RuntimeError('Incompatible model classes')
number_to_label={v:k for k,v in label_to_number.items()}
clean_text('resource check')
def predict_text(text):
    if not isinstance(text,str) or not text.strip():raise ValueError('Non-empty text required')
    cleaned=clean_text(text)
    if not cleaned.strip():raise ValueError('No usable text remains')
    x=vectorizer.transform([cleaned])
    prediction=int(model.predict(x)[0])
    score=float(model.predict_proba(x)[0,list(model.classes_).index(1)])
    return {'prediction':number_to_label[prediction],'model_score':score,'cleaned_text':cleaned}
