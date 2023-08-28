
## Visualization API - REST API to link BmnRoot and VisionForge


### Setup

To start working, clone this repo, then:
```
cd visapi
python3.6 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

To run development server on port 50000:
```
source env/bin/activate
python app.py
```

To run in background even when user logs out:
```
source env/bin/activate
nohup python app.py &
```

### API Calls

To get geometry JSON:

```
GET /geometry/<period>/<run>
```
(e.g. `/geometry/8/8000`, `/geometry/7/2076` should work).


To get particle tracks JSON for event:

```
GET /event/<event_idx>
```
(e.g. `/event/0`, `/event/1` and all other indexes less than `dataChain->GetEntries()`).
