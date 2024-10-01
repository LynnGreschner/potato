import json
import pandas as pd


# Angenommen, Ihre CSV-Dateien befinden sich im selben Verzeichnis wie dieses Skript und sind wie folgt benannt: 'file1.csv', 'file2.csv', ..., 'file10.csv'
csv_files = [f'main_defabel_{i}.csv' for i in range(1, 11)]

for i, file in enumerate(csv_files, 1):
    df = pd.read_csv(file)

    # Daten für JSON-Datei vorbereiten
    data = []
    for index, row in df.iterrows():
        entry = {
            "id": str(index + 1),
            "text": "<div class='instruction'><span class='working_example' /><p>Lesen Sie sich die folgende Aussage durch:</p>\n<p class='statement'>Aussage: " + row['statement'] + "</p>\n<p>Lesen Sie sich jetzt das folgende Argument sorgf&auml;ltig durch. Danach beantworten Sie bitte die nachfolgenden Fragen.</p></div><div class='argument'>\n<b>Argument:</b> " + row['arguments'] + "</div>\n",
            # Hier können Sie zusätzliche Informationen aus der CSV-Datei hinzufügen
            "meta_info_original_defabel": {
                "instance_id": row['instance_id'],
                "participant_id": row['participant_id'],
                "qid": row['qid'],
                "instruction": row['instruction'],
                "topic_familiarity": row['topic_familiarity'],
                "author_confidence": row['author_confidence'],
                "author_belief": row['author_belief'],
                "is_factual": row['is_factual'],
                "is_deception": row['is_deception']
            }
        }
        data.append(entry)

    # JSON-Datei erstellen
    with open(f'data_main_defabel_{i}.json', 'w', encoding='utf-8') as f:
        for entry in data:
            json.dump(entry, f, ensure_ascii=False)
            f.write('\n')