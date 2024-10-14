import os
import json
import pandas as pd

directory = '/home/ba7nq8/potato/project-hub/defabel_emo_conv/anno_output_test'

df_list = []
passed_ids = []

# Existing code...

for item in os.listdir(directory):
    item_path = os.path.join(directory, item)

    if os.path.isdir(item_path):
        filepath = os.path.join(item_path, 'annotated_instances.jsonl')

        if os.path.exists(filepath):

            with open(filepath) as f:
                for line in f:

                    data = json.loads(line)

                    if data['id'].startswith('test_question_testing_'):

                        if (list(data['label_annotations']['stance'].keys())[0] ==  data['id'].split('_')[-1] and
                            data['label_annotations']['topic_familiarity'] == {"Ich würde es sehr gerne vermeiden, über dieses Thema zu sprechen.": "1"} and
                            data['label_annotations']['convincingness'] == {"1": "1"} and
                            data['label_annotations']['emotion_binary'] == {"Ja.": "1"}):
                            passed_ids.append(item)
                        else:
                            print(f"Attention check failed for annotator {item}.")
                    
                    if data['id'].isdigit() and item in passed_ids:
                        emotion_value = list(data['label_annotations'].get('emotion', {}).values())[0].split(':::')[-1] if data['label_annotations'].get('emotion') else None
                        
                        # The following code will load the assigned_user_data.json file and store the meta_info_original_defabel value
                        assigned_user_data_filepath = os.path.join(item_path, 'assigned_user_data.json')

                        if os.path.exists(assigned_user_data_filepath):
                            with open(assigned_user_data_filepath) as f:
                                assigned_user_data = json.load(f)
                            
                                if data['id'] in assigned_user_data:
                                    meta_info_original_defabel = assigned_user_data[data['id']].get('meta_info_original_defabel', None)
                                else:
                                    meta_info_original_defabel = None
                        else:
                            print(f"No assigned_user_data.json file in directory {item_path}. Skipping this id.")
                        
                        df_list.append(pd.DataFrame({
                            'id': [data['id']],
                            'text': [data['displayed_text']],
                            'stance': [list(data['label_annotations']['stance'].values())[0]],
                            'topic_familiarity': [list(data['label_annotations']['topic_familiarity'].values())[0]],
                            'convincingness': [list(data['label_annotations']['convincingness'].values())[0]],
                            'emotion_binary': [list(data['label_annotations']['emotion_binary'].values())[0]],
                            'emotion': [emotion_value],
                            'meta_info_original_defabel': [meta_info_original_defabel]  # Add the meta_info_original_defabel value to the DataFrame
                        }))
        else:
            print(f"No annotated_instances.jsonl file in directory {item_path}. Skipping this directory.")

# Existing code...


# Add a check here to see if df_list is not empty before trying to concatenate it
if df_list:
    df = pd.concat(df_list, ignore_index=True)

    if not df.empty:
        df = df.groupby(['id', 'text']).agg({
            'stance': list,
            'topic_familiarity': list,
            'convincingness': list,
            'emotion_binary': list,
            'emotion': list,
            'meta_info_original_defabel': list
        }).reset_index()

        df.to_csv('TEST_output_data.csv', index=False)
else:
    print("No data was read into the DataFrame.")

with open('TEST_passed_ids.tsv', 'w') as f:
    for id in passed_ids:
        f.write(id + '\n')

