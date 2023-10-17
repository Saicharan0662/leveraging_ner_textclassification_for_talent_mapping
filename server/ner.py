import spacy
import random

# nlp_custom = spacy.load(r"./output_320ds/model-best")
nlp_custom = spacy.load(r"./output_1200ds/model-best")
nlp = spacy.load("en_core_web_sm")


class NER():
    def __init__(self, text):
        self.text = text
        self.sentence_range_list = []

    def get_formated_text(self):
        doc = nlp(self.text)
        sentence = list(doc.sents)

        for i in range(len(sentence)):
            if i == 0:
                self.sentence_range_list = [(0, len(str(sentence[0])))]
            else:
                self.sentence_range_list.append(
                    (self.sentence_range_list[i-1][1], self.sentence_range_list[i-1][1]+1 + len(str(sentence[i]))))

        result = []
        for token in sentence:
            doc = nlp_custom(token.text)
            for ent in doc.ents:
                res = (token.text, ent.text, ent.label_)
                result.append(res)

        return {"res": result}

    def get_sentence_no(self, l, r):
        for i in range(len(self.sentence_range_list)):
            l1, r1 = self.sentence_range_list[i]
            if l >= l1 and r < r1:
                return i

        return -1
