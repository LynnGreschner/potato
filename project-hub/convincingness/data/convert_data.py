import json

# Open the file and load the data
with open('real_data_snippets.json', 'r') as file:
    data = json.load(file)

# Write the data back to the file with UTF-8 encoding
with open('real_data_snippets_utf8.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)
