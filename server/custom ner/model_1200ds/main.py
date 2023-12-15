import json
import spacy
from spacy.tokens import DocBin
from tqdm import tqdm


data = json.load(open('annotations.json'))
jtopy = json.dumps(data)
dict_json = json.loads(jtopy)
train = dict_json["annotations"]


nlp = spacy.blank("en")
db = DocBin()
for text, annot in tqdm(train):
    print(text, annot)
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annot["entities"]:
        span = doc.char_span(start, end, label=label,
                             alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("./train.spacy")
