import os
import json
import pandas as pd

# Define the directory where the JSON files are located
# directory = '/home/ba7nq8/potato/project-hub/defabel_emo_conv/anno_output_prelim1'
directory = '/home/ba7nq8/potato/project-hub/defabel_emo_conv/annotation_output'

# Initialize an empty list to store DataFrame
df_list = []

# Initialize a list to store the IDs of the annotators who passed the attention check
passed_ids = []

# Loop through each item in the directory
for item in os.listdir(directory):
    # Construct the path to the item
    item_path = os.path.join(directory, item)

    # Check if the item is a directory
    if os.path.isdir(item_path):
        # Construct the path to the JSON file
        filepath = os.path.join(item_path, 'annotated_instances.jsonl')

        # Open the file
        with open(filepath) as f:
            # Each line in the file is a separate JSON object
            for line in f:
                data = json.loads(line)

                # Check if the file is an attention check
                if data['id'].startswith('test_question_testing_'):
                    # Check if the attention check is passed
                    if (data['label_annotations']['stance'] == {data['id'].split('_')[-1]: "4"} and
                        data['label_annotations']['topic_familiarity'] == {"Ich würde es sehr gerne vermeiden, über dieses Thema zu sprechen.": "1"} and
                        data['label_annotations']['convincingness'] == {"1": "1"} and
                        data['label_annotations']['emotion_binary'] == {"Ja.": "1"}):
                        # If the attention check is passed, add the annotator's ID to the list
                        passed_ids.append(item)
                    else:
                        print(f"Attention check failed for annotator {item}.")
                
                # If the id is numeric (i.e., the file is not an attention check), add the data to the DataFrame
                if data['id'].isdigit():
                    emotion_value = list(data['label_annotations'].get('emotion', {}).values())[0].split(':::')[-1] if data['label_annotations'].get('emotion') else None
                    df_list.append(pd.DataFrame({
                        'id': [data['id']],
                        'text': [data['displayed_text']],
                        'stance': [list(data['label_annotations']['stance'].values())[0]],
                        'topic_familiarity': [list(data['label_annotations']['topic_familiarity'].values())[0]],
                        'convincingness': [list(data['label_annotations']['convincingness'].values())[0]],
                        'emotion_binary': [list(data['label_annotations']['emotion_binary'].values())[0]],
                        'emotion': [emotion_value]
                    }))

# Concatenate all the dataframes in the list
df = pd.concat(df_list, ignore_index=True)

# Check if the DataFrame is not empty
if not df.empty:
    # Group the DataFrame by id and text, and aggregate the other columns
    df = df.groupby(['id', 'text']).agg({
        'stance': list,
        'topic_familiarity': list,
        'convincingness': list,
        'emotion_binary': list,
        'emotion': list
    }).reset_index()

    # Write the DataFrame to a CSV file
    df.to_csv('output_data.csv', index=False)

# Write the IDs of the annotators who passed the attention check to a file
with open('passed_ids.tsv', 'w') as f:
    for id in passed_ids:
        f.write(id + '\n')

if df.empty:
    print("No data was read into the DataFrame.")
