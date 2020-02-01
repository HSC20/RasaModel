import csv, json

csvfile = open('C:/Users/Harpreet/.newenv/exp.csv', 'r')

common_examples = []

fieldnames = ("Expression", "Intent")
reader = csv.DictReader(csvfile, fieldnames)

for row in reader:
    common_examples.append(row)

del common_examples[0]  # remove header row

# construct the required json structure
rasa_nlu_data = {"common_examples": common_examples}
json_data = {"rasa_nlu_data": rasa_nlu_data}

# The result file that will be fed into rasa for training
with open('intentClassifiedFile.json', 'w') as fp:
    json.dump(json_data, fp)
from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("C:/Users/Harpreet/.newenv/models/nlu-20200201-012330/nlu")
print(json.dumps(interpreter.parse("how are you"))