from flask import Flask, render_template, request, jsonify
from algorithm import a_star

app = Flask(__name__)

GRID = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,1,1,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,1,1,0,1,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,1,0,1,0,1,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0],
]

LOCATIONS = {"A":(0,0),"B":(0,9),"C":(2,2),"D":(4,7),"E":(6,0),"F":(8,4),"G":(8,9),"H":(9,9)}
AMBULANCES = {"Ambulance 1":"A", "Ambulance 2":"B"}
PATIENTS = {"Patient A":"C", "Patient B":"D", "Patient C":"E"}
HOSPITALS = {"City Hospital":"H", "Central Hospital":"G", "Emergency Hospital":"F"}

@app.route("/")
def index():
    return render_template("index.html", rows=len(GRID), cols=len(GRID[0]), ambulances=AMBULANCES, patients=PATIENTS, hospitals=HOSPITALS)

@app.post("/api/route")
def calculate_route():
    try:
        data = request.get_json(force=True)
        a = data.get("ambulance"); p = data.get("patient"); h = data.get("hospital")
        if a not in AMBULANCES or p not in PATIENTS or h not in HOSPITALS:
            return jsonify(error="Please select valid ambulance, patient and hospital."), 400
        start = LOCATIONS[AMBULANCES[a]]; patient = LOCATIONS[PATIENTS[p]]; hospital = LOCATIONS[HOSPITALS[h]]
        if len({start, patient, hospital}) < 3:
            return jsonify(error="Please choose different locations for ambulance, patient and hospital."), 400
        pickup, e1 = a_star(GRID, start, patient)
        if not pickup:
            return jsonify(error="No route is available from the ambulance to the patient."), 404
        hospital_path, e2 = a_star(GRID, patient, hospital)
        if not hospital_path:
            return jsonify(error="No route is available from the patient to the hospital."), 404
        full = pickup + hospital_path[1:]
        return jsonify(ambulance=list(start), patient=list(patient), hospital=list(hospital), pickup_path=[list(x) for x in pickup], hospital_path=[list(x) for x in hospital_path], full_path=[list(x) for x in full], pickup_cost=len(pickup)-1, hospital_cost=len(hospital_path)-1, total_cost=len(pickup)-1+len(hospital_path)-1, nodes_explored=e1+e2, algorithm="A* Search", heuristic="Manhattan Distance")
    except Exception as exc:
        return jsonify(error=f"Server error: {exc}"), 500

if __name__ == "__main__":
    app.run(debug=True)
