# AI Emergency Ambulance Route Planner

College mini-project using Flask, HTML/CSS/JavaScript and A* Search.

## Run on Windows

Open this folder in VS Code, then Terminal -> New Terminal:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open Chrome and visit:

`http://127.0.0.1:5000`

## Project structure

```text
AI_Ambulance_Route_Planner/
├── app.py
├── algorithm.py
├── requirements.txt
├── README.md
├── templates/index.html
└── static/
    ├── style.css
    └── script.js
```

## AI concepts

- Intelligent Agent: ambulance
- Environment: simulated road grid
- State Space: grid cells
- Informed Search: A*
- Heuristic: Manhattan distance
- Planning: ambulance -> patient -> hospital

This is an academic simulation, not a real emergency dispatch or navigation system.
