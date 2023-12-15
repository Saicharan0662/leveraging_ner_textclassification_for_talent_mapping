import spacy

nlp = spacy.load(r"./output/model-best")

doc = nlp(
    "Contributed in the automatic documentation process for the code using Sphinx")

for ent in doc.ents:
    print(ent.text, ent.label_)
