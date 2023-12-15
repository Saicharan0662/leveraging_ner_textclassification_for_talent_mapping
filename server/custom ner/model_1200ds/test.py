import spacy

nlp = spacy.load(r"./output/model-best")

doc = nlp(
    "Runner-up position at MongoDB competition")

for ent in doc.ents:
    print(ent.text, ent.label_)
