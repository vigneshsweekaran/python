import json

output_data = {}

with open("data.json") as jsonFile:
    data = json.load(jsonFile)
    jsonFile.close()

for key, patient_data in data.items():
    if patient_data["status"] == "alive" and patient_data["age"] > 50:
        if patient_data["disease"] in output_data:
            present_count = int(output_data[patient_data["disease"]])
            output_data[patient_data["disease"]] = present_count+1
        else:
          output_data[patient_data["disease"]] = 1

for disease, count in output_data.items():
    print(f"{disease} : {count}")
        

