#from rasa_nlu.training_data import load_data
#from rasa_nlu.config import RasaNLUConfig
# from rasa_nlu.model import Trainer
# from rasa_nlu.model import Metadata, Interpreter
# from rasa_nlu import config
import csv, json
from rasa_nlu.model import Interpreter
import json

csvfile = open('C:/Users/Harpreet/.newenv/exp.csv', 'r')

common_examples = []

fieldnames = ("Expression", "Intent")
reader = csv.DictReader(csvfile, fieldnames)
interpreter = Interpreter.load("C:/Users/Harpreet/.newenv/models/nlu-20200201-012330/nlu")
print(json.dumps(interpreter.parse("how are you")["intent"], indent=2)
for row in reader:
    common_examples.append(row)

del common_examples[0]
rasa_nlu_data = {"common_examples": common_examples}
json_data = {"rasa_nlu_data": rasa_nlu_data}
with open('intentClassifiedFile.json', 'w') as fp:
    json.dump(json_data, fp)






#from rasa.nlu.extractors.crf_entity_extractor import CRFEntityExtractor
#crf = CRFEntityExtractor()
# train_data=load_data("C:/Users/Harpreet/.newenv/default/model_20200130-015517/training_data.json")
# trainer =Trainer(config.load("C:/Users/Harpreet/.newenv/config.yml"))
# #trainer.train(train_data)
#
# #print(trainer.train(train_data))
#
# model_directory = trainer.persist(‪"C:/Users/Harpreet/.newenv/models/20200128-152628/core/policy_1_KerasPolicy/keras_model.h5")
# rasa_nlu_data = {"common_examples" : common_examples}
# json_data = {"rasa_nlu_data" : rasa_nlu_data}
#
# with open('intentClassifiedFile.json', 'w') as fp:
#     json.dump(json_data, fp)
# # crf = CRFEntityExtractor()
# def filter_trainable_entities(self, entity_examples):
#     for ent in message.get("entities", []):
#         extractor = ent.get("extractor")
#         if not extractor or extractor == self.name:
#             entities.append(ent)
#
# entities =  [entity["start"], entity["end"], entity["entity"]]
# for ent in example.get("entities", []):
#     (31, 37, 'location'), (10, 17, 'cuisine')
# x=input("question")
# features = crf._sentence_to_features(x)
# ents = crf.ent_tagger.predict_marginals_single(features)

# import spacy
# nlp=spacy.load('en')
# docs=nlp("I am looking for a Italian Restaurant")
#
# for word in docs.ents:
#     print("value",word.text,"entity",word.label,"start",word.start_char,"end",word.end_char)

