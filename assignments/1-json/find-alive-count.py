import json

output_data = {}

with open("data.json") as jsonFile:
    data = json.load(jsonFile)
    jsonFile.close()

for patient_name, patient_data in data.items():
    if patient_data["status"] == "alive" and patient_data["age"] > 50:
        if patient_data["disease"] in output_data:
            present_count = int(output_data[patient_data["disease"]]["count"])
            output_data[patient_data["disease"]]["count"] = present_count+1
            output_data[patient_data["disease"]]["patient_names"].append(patient_name)
        else:
          output_data[patient_data["disease"]] = {"count": "1", "patient_names": [patient_name]}

for disease, details in output_data.items():
    count = details["count"]
    patient_names = ", ".join(details["patient_names"])
    print(f" No of patient's infected with {disease} is {count} and the patient names are {patient_names}")
