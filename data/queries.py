import json
import os

directory = './matches'
for filename in os.listdir(directory)[0:1]:
    # Cargar JSON como objeto
    with open(os.path.join(directory, filename), 'r') as file:
        match = json.load(file)
        print(match['matchId'])


