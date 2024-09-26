import json

# Open the file and load the data
with open('project-hub/defabel_emo_conv/data/data_prelim1.json', 'r') as file:
    data = json.load(file)

# Write the data back to the file with UTF-8 encoding
with open('project-hub/defabel_emo_conv/data/data_prelim1_utf-8.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)
