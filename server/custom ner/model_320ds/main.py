import json
import spacy
from spacy.tokens import DocBin
from tqdm import tqdm

# file = open('annotations.json')
data = json.load(open('annotations.json'))
# json.dumps take a dictionary as input and returns a string as output.
jtopy = json.dumps(data)
# json.loads take a string as input and returns a dictionary as output.
dict_json = json.loads(jtopy)
# print(dict_json["annotations"])
train = dict_json["annotations"]


nlp = spacy.blank("en")
db = DocBin()  # create a DocBin object
for text, annot in tqdm(train):  # data in previous format
    print(text, annot)
    doc = nlp.make_doc(text)  # create doc object from text
    ents = []
    for start, end, label in annot["entities"]:  # add character indexes
        span = doc.char_span(start, end, label=label,
                             alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents  # label the text with the ents
    db.add(doc)
db.to_disk("./train.spacy")  # save the docbin object
